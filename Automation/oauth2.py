import os
import time
import urllib.error
import urllib.request
import psutil
import schedule
from sys import argv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import base64

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def is_connected():
    try:
        urllib.request.urlopen("http://www.google.com", timeout=5)
        return True
    except urllib.error.URLError as err:
        print(f"No internet connection. Error: {err}")
        return False

def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def create_message_with_attachment(sender, to, subject, message_text, file):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg = MIMEText(message_text)
    message.attach(msg)

    with open(file, 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={os.path.basename(file)}',
        )
        message.attach(part)

    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode()
    return {'raw': raw}

def send_message(service, user_id, message):
    try:
        sent_message = (service.users().messages().send(userId=user_id, body=message).execute())
        print(f'Message Id: {sent_message["id"]}')
        return sent_message
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

def MailSender(filename, log_time):
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)
    
    fromaddr = "varad.burner@gmail.com"
    toaddr = "varad.chaskar.27@gmail.com"
    subject = f"subject {log_time}"
    body = f"Hi hello Bye {toaddr} {log_time}"

    message = create_message_with_attachment(fromaddr, toaddr, subject, body, filename)
    send_message(service, 'me', message)

def ProcessLog(log_dir="Marvellous"):
    listprocess = []
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    separator = "-" * 80
    log_filename = f"MarvellousLog{time.ctime().replace(' ', '_').replace(':', '_')}.log"
    log_path = os.path.join(log_dir, log_filename)
    with open(log_path, 'w') as f:
        f.write(separator + "\n")
        f.write("Mar Process logger: " + time.ctime() + "\n")
        f.write(separator + "\n")
        f.write("\n")

        for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
                vms = proc.memory_info().vms / (1024 * 1024)
                pinfo['vms'] = vms
                listprocess.append(pinfo)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        for element in listprocess:
            f.write("%s\n" % element)

    print("Log file generated at the location %s" % log_path)

    connected = is_connected()

    if connected:
        start_time = time.time()
        MailSender(log_path, time.ctime())
        end_time = time.time()
        print("Took %s seconds to send the mail" % (end_time - start_time))
    else:
        print("There is no internet connection")

def main():
    print("Application Name: " + argv[0])
    if len(argv) != 2:
        print("Error: Incorrect number of arguments. Usage: <script> <interval_in_minutes>")
        exit(1)
    try:
        interval = int(argv[1])
        print(f"Scheduling ProcessLog every {interval} minutes...")
        schedule.every(interval).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError:
        print("Error: Invalid datatype for interval. It should be an integer.")
    except Exception as e:
        print("Error: Exception", e)

if __name__ == "__main__":
    main()
