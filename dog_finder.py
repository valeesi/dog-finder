import time
import hashlib
import smtplib
import secrets.mail as mail
from email.mime.text import MIMEText
from pyquery import PyQuery as pq

from email.mime.multipart import MIMEMultipart

time_out = 10
d = pq('https://hundarutanhem.se/dog/category/sma-hundar/')
first_dog_href = d("article").eq(0).find('a').attr("href")
first_dog_img = d("article").eq(0).find('a').find("img").attr("src")

currentHash = hashlib.sha224(d("article").__str__().encode("utf-8")).hexdigest()
print("Dog finder launched")

msg = MIMEMultipart("First dog")
msg['Subject'] = "Test sent from Python"
msg['From'] = mail.username
msg['To'] = ", ".join(mail.recipients)
msgText = MIMEText(
    '<a href="https://hundarutanhem.se/hundar/pigga-21-0256/"><img src="https://hundarutanhem.se/wp-content/uploads/2021/03/Pigga-21-0256_003.jpg" alt=""></a>',
    'html')
msg.attach(msgText)

mail_server = smtplib.SMTP('smtp.office365.com', 587)
mail_server.ehlo()
mail_server.starttls()
mail_server.ehlo()
mail_server.login(mail.username, mail.password)
mail_server.send_message(msg)
mail_server.close()

#
# while True:
#     try:
#         time.sleep(time_out)
#         d = pq('https://hundarutanhem.se/dog/category/sma-hundar/')
#         newHash = hashlib.sha224(d("article").__str__().encode("utf-8")).hexdigest()
#         if newHash == currentHash:
#             continue
#         else:
#             print("Something changed")
#             mail_server.send_message(msg)
#             continue
#     except Exception as e:
#         print("error: " + e)
