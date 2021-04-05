import time
import hashlib
from pyquery import PyQuery as pq
import mail.factory as mail
import data.zoo as data

time_out = 10

def hash(str):
    return hashlib.sha224(str).hexdigest()


def add_dog(url, tag_for_list, additional_tag=None):
    d = pq(url)
    for dog in d.items(tag_for_list):
        if additional_tag is None:
            dog_entry = dog
        else:
            dog_entry = dog.find(additional_tag)
        data.dogs_found.add(
            hash(dog_entry.__str__().encode("utf-8"))
        )

def load_current_dogs():
    for site, value in data.sites_to_monitor.items():
        if site == 'hundarutanhem':
            add_dog(value['url'], 'article', additional_tag='a')
        elif site == 'hundarsokerhem':
            add_dog(value['url'], value['tag'])


print("Dog finder launched")
strr = load_current_dogs()
# mail.SendMail("New dogs found", strr)
print("Mail sent")

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
