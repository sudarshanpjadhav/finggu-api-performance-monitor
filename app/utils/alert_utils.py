import smtplib
from email.mime.text import MIMEText
import os


def finggu_send_alert(subject, message):
    fingguVar_email = os.getenv('ALERT_EMAIL')
    fingguVar_password = os.getenv('ALERT_PASSWORD')
    fingguVar_smtp_server = os.getenv('SMTP_SERVER')
    fingguVar_smtp_port = os.getenv('SMTP_PORT')

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = fingguVar_email
    msg['To'] = fingguVar_email

    with smtplib.SMTP(fingguVar_smtp_server, fingguVar_smtp_port) as server:
        server.starttls()
        server.login(fingguVar_email, fingguVar_password)
        server.send_message(msg)
