import smtplib
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email():
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(receiver_emails)
    message['Subject'] = 'This is the subject of the email.'  # Subject

    # The body of the email
    mail_content = body_content

    # Adding the content to the mail
    message.attach(MIMEText(mail_content, 'plain'))

    # Attach file, if the user wants to
    if attach_file.lower() in ['yes', 'y']:
        try:
            with open(file_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)

            # Add header as pdf attachment
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(file_path)}",
            )

            message.attach(part)
        except Exception as e:
            print(f'Attachment failed due to error: {e}')
    
    try:
        # Use the provided SMTP server
        server = smtplib.SMTP(smtp_server, 587)
        server.starttls()

        # Login to the account
        server.login(sender_email, password)
        
        # Send the email
        text = message.as_string()
        server.sendmail(sender_email, receiver_emails, text)
        server.quit()
        print('Mail Sent')
    except Exception as e:
        print(f'Mail failed due to error: {e}')


# User input
sender_email = input("Enter your email: ")
password = getpass("Enter your password: ")  # Secure way to handle password input
receiver_emails = input("Enter email(s) to send to (separated by commas if more than one): ").split(',')
body_content = input("Enter the body of the email: ")
attach_file = input("Do you want to attach a file? (Yes/No): ")
if attach_file.lower() in ['yes', 'y']:
    file_path = input("Enter the path of the file to attach: ")
smtp_server = input("Enter the SMTP server (e.g. 'smtp.gmail.com' for Gmail, 'smtp.mail.yahoo.com' for Yahoo): ")

# Send the email
send_email()