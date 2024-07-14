import os
import psutil
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

def create_log_file(directory, log_filename="process_log.txt"):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    log_filepath = os.path.join(directory, log_filename)
    
    with open(log_filepath, 'w') as log_file:
        log_file.write(f"{'PID':<10} {'Name':<25} {'Username'}\n")
        log_file.write("="*50 + "\n")
        
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                log_file.write(f"{proc.info['pid']:<10} {proc.info['name']:<25} {proc.info['username']}\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    
    return log_filepath

def send_email(log_filepath, recipient_email):
    sender_email = ""
    sender_password = ""
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Process Log File"
    
    body = "Attached is the log file containing information about running processes."
    msg.attach(MIMEText(body, 'plain'))
    
    attachment = MIMEBase('application', 'octet-stream')
    with open(log_filepath, 'rb') as log_file:
        attachment.set_payload(log_file.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f"attachment; filename={os.path.basename(log_filepath)}")
    msg.attach(attachment)
    
    try:
        server = smtplib.SMTP('', )
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ProcInfoLog.py <Directory> <Recipient Email>")
        sys.exit(1)
    
    directory = sys.argv[1]
    recipient_email = sys.argv[2]
    
    log_filepath = create_log_file(directory)
    send_email(log_filepath, recipient_email)
