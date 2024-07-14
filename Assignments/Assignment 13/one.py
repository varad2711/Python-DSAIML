import os
import sys
import hashlib
import datetime
import time
import psutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

# Directory and Log Management
def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def get_log_file_path(base_directory):
    create_directory(base_directory)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"duplicate_log_{timestamp}.txt"
    return os.path.join(base_directory, log_filename)

def write_log(message, log_file_path):
    with open(log_file_path, 'a') as log_file:
        log_file.write(message + "\n")

def calculate_checksum(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
    except Exception as e:
        return None
    return sha256.hexdigest()

# File Deduplication
def find_and_remove_duplicates(directory, log_file_path):
    files_checksums = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_checksum = calculate_checksum(file_path)
            if file_checksum:
                if file_checksum in files_checksums:
                    duplicates.append(file_path)
                else:
                    files_checksums[file_checksum] = file_path

    for duplicate in duplicates:
        try:
            os.remove(duplicate)
            write_log(f"Deleted duplicate file: {duplicate}", log_file_path)
        except Exception as e:
            write_log(f"Failed to delete {duplicate}: {e}", log_file_path)

    return len(files_checksums), len(duplicates)

# Email Functionality
def send_email(log_filepath, recipient_email, subject, body):
    sender_email = "youremail@example.com"  # Replace with your email
    sender_password = "yourpassword"  # Replace with your email password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    attachment = MIMEBase('application', 'octet-stream')
    with open(log_filepath, 'rb') as log_file:
        attachment.set_payload(log_file.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f"attachment; filename={os.path.basename(log_filepath)}")
    msg.attach(attachment)

    try:
        server = smtplib.SMTP('smtp.example.com', 587)  # Replace with your SMTP server and port
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Scheduler
def schedule_task(interval_minutes, task, *args, **kwargs):
    interval_seconds = interval_minutes * 60
    while True:
        task(*args, **kwargs)
        time.sleep(interval_seconds)

# Main Execution
def main(directory, interval_minutes, recipient_email):
    marvellous_dir = "Marvellous"
    create_directory(marvellous_dir)
    log_file_path = get_log_file_path(marvellous_dir)

    def task():
        start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        num_files_scanned, num_duplicates = find_and_remove_duplicates(directory, log_file_path)
        end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_message = (
            f"Starting time of scanning: {start_time}\n"
            f"Total number of files scanned: {num_files_scanned}\n"
            f"Total number of duplicate files found: {num_duplicates}\n"
            f"Ending time of scanning: {end_time}\n"
        )
        write_log(log_message, log_file_path)

        email_body = (
            f"Starting time of scanning: {start_time}\n"
            f"Total number of files scanned: {num_files_scanned}\n"
            f"Total number of duplicate files found: {num_duplicates}\n"
            f"Ending time of scanning: {end_time}\n"
        )
        send_email(log_file_path, recipient_email, "Duplicate File Removal Log", email_body)

    schedule_task(interval_minutes, task)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: DuplicateFileRemoval.py <Directory> <Interval Minutes> <Recipient Email>")
        sys.exit(1)

    directory = sys.argv[1]
    try:
        interval_minutes = int(sys.argv[2])
    except ValueError:
        print("Invalid interval. Please enter a number.")
        sys.exit(1)

    recipient_email = sys.argv[3]
    main(directory, interval_minutes, recipient_email)
