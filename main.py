import data.zoo as zoo
import time
from logging_config import logger
from mail.factory import SendMail


def main():
    logger.info("Launching...")
    logger.info("Search for dogs on " + len(zoo.sites_to_monitor.items()).__str__() + " sites")
    zoo.scan_for_dogs()
    logger.info(len(zoo.current_dogs).__str__() + " dogs have been added to cache")
    zoo.new_dogs.clear()
    logger.info("Monitoring...")
    while True:
        try:
            time.sleep(600)
            zoo.scan_for_dogs()
            if len(zoo.new_dogs) == 0:
                logger.info("No updates...")
                continue
            else:
                notis = len(zoo.new_dogs.values()).__str__() + " new dog(s) found"
                SendMail(notis, "".join(zoo.new_dogs.values()))
                logger.info(notis)
                zoo.new_dogs.clear()
                continue
        except Exception as e:
            logger.error("Error: " + e)


if __name__ == "__main__":
    main()
