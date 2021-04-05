import data.zoo as zoo
import time
from logging_config import logger
from mail.factory import SendMail


def main():
    logger.info("Launching...")
    zoo.scan_for_dogs()
    zoo.new_dogs.clear()
    logger.info("Monitoring...")
    while True:
        try:
            time.sleep(300)
            zoo.scan_for_dogs()
            if len(zoo.new_dogs) == 0:
                continue
            else:
                notis = len(zoo.new_dogs.values()).__str__() + " new dogs found"
                SendMail(notis, "".join(zoo.new_dogs.values()))
                logger.info(notis)
                zoo.new_dogs.clear()
                continue
        except Exception as e:
            logger.error("Error: " + e)


if __name__ == "__main__":
    main()
