import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess
import socket

# Email configuration
email_user = 'user@user.com' # Replace with the email user
email_password = 'pass'  
email_smtp_server = 'smtp.office365.com' # Replace with your smtp server
email_smtp_port = 465
email_receiver = ''  add receiver's email here 


def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_receiver
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP_SSL(email_smtp_server, email_smtp_port)
        server.login(email_user, email_password)
        text = msg.as_string()
        server.sendmail(email_user, email_receiver, text)
        server.quit()
        print(f"Email sent: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")




if __name__ == "__main__":
    send_email("Subject", "Body")
