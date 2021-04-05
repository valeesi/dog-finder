import time
import hashlib
from pyquery import PyQuery as pq
import mail.factory as mail

time_out = 10
d = pq('https://hundarutanhem.se/dog/category/sma-hundar/')
first_dog_href = d("article").eq(0).find('a').attr("href")
first_dog_img = d("article").eq(0).find('a').find("img").attr("src")

currentHash = hashlib.sha224(d("article").__str__().encode("utf-8")).hexdigest()
print("Dog finder launched")

mail.SendMail("New dogs found", d("article").eq(0).__str__())

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
