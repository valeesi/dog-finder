import time
import hashlib
import smtplib
import secrets.mail as mail
from urllib.request import urlopen, Request
from email.mime.text import MIMEText

dog_website = "https://www.reddit.com/new/"
time_out = 10
url = Request(dog_website, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(url).read()
currentHash = hashlib.sha224(response).hexdigest()
print("Dog finder launched")

msg = MIMEText("Random text", 'plain')
msg['Subject'] = "Test sent from Python"
msg['From'] = mail.username
msg['To'] = ", ".join(mail.recipients)

mail_server = smtplib.SMTP('smtp.office365.com', 587)
mail_server.ehlo()
mail_server.starttls()
mail_server.ehlo()
mail_server.login(mail.username, mail.password)

while True:
    try:
        time.sleep(time_out)
        response = urlopen(url).read()
        newHash = hashlib.sha224(response).hexdigest()

        if newHash == currentHash:
            continue
        else:
            print("Something changed")
            mail_server.send_message(msg)
            continue
    except Exception as e:
        print("error: " + e)
