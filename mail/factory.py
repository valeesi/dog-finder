import os

import secrets.mail as mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from pyquery import PyQuery as pq


class SendMail:
    def __init__(self, subject, html_content):
        mail_server = smtplib.SMTP('smtp.office365.com', 587)
        mail_server.ehlo()
        mail_server.starttls()
        mail_server.ehlo()
        mail_server.login(mail.username, mail.password)

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = formataddr(('Dog finder', mail.username))
        msg['To'] = ", ".join(mail.recipients)

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, "template.html"), "r") as f:
            contents = f.read()
            template = pq(contents)

        template.find(".dog-list").append(html_content)

        msg_text = MIMEText(template.__str__(), 'html')
        msg.attach(msg_text)

        mail_server.send_message(msg)
        mail_server.close()
