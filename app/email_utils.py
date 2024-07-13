import smtplib
from email.mime.text import MIMEText
import os

def send_email(email):
    sender = os.getenv('GMAIL_USER')
    password = os.getenv('GMAIL_PASSWORD')
    recipient = email

    subject = 'HNG11-DevOps password reset'
    body = """
    Dear ThePrimeJnr,

    We’ve received your request to reset your password. Please click the link below to complete the reset.

    Reset(dummy link attached)

    If you need additional assistance or did not make this change, don't hesitate to contact destiny@destinedcodes.com.
    """

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, [recipient], msg.as_string())
        print(f'Email sent to {recipient}')
    except Exception as e:
        print(f'Failed to send email to {recipient}: {e}')

