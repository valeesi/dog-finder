import time
import hashlib
import smtplib
import secrets.mail as mail
from urllib.request import urlopen, Request
from email.mime.text import MIMEText
from html.parser import HTMLParser
from pyquery import PyQuery as pq
from lxml import etree
import urllib


dog_website = "https://hundarutanhem.se/dog/category/sma-hundar/"
time_out = 10
url = Request(dog_website, headers={'User-Agent': 'Mozilla/5.0'})

response = urlopen(url).read().decode("utf-8")
# d = pq(response)
d = pq('https://hundarutanhem.se/dog/category/sma-hundar/')
first_dog_href = d("article").eq(0).find('a').attr("href")
first_dog_img = d("article").eq(0).find('a').find("img").attr("src")

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
