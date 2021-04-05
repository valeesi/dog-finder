import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import secrets.mail as mail


class SendMail:
    def __init__(self, subject, html_content):
        mail_server = smtplib.SMTP('smtp.office365.com', 587)
        mail_server.ehlo()
        mail_server.starttls()
        mail_server.ehlo()
        mail_server.login(mail.username, mail.password)

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = mail.username
        msg['To'] = ", ".join(mail.recipients)
        msg_text = MIMEText(html_content, 'html')
        msg.attach(msg_text)

        mail_server.send_message(msg)
        mail_server.close()
