import smtplib, ssl
import os


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    username = os.getenv("GMAIL_ACC")
    password = os.getenv("GMAIL_PASSWORD")
    context = ssl.create_default_context()
    receiver_email = os.getenv("GMAIL_ACC")

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        # Send the email with proper encoding
        server.sendmail(username, receiver_email, message.encode('utf-8'))


