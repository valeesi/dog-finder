import data.zoo as zoo
import time
from datetime import datetime
from logging_config import logger
from mail.factory import SendMail


def main():
    time_out = 10
    logger.info("Dog finder launched")
    zoo.load_current_dogs()
    # SendMail("New dogs found", strr)
    logger.info("Mail sent")

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


if __name__ == "__main__":
    main()
