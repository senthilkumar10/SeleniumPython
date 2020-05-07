import logging

logging.basicConfig(filename="./logs/test.log",
                    format = "%(asctime)s: %(levelname)s: %(message)s",
                    datefmt="%m/%d/%y %I:%m:%s %p")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is Debug Message")

logger.info("This is info Message")

logger.warning("This is warning Message")

logger.error("This is error message")

logger.critical("This is critial message")