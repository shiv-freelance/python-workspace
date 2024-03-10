import logging

logging.basicConfig(filename="person.log", level=logging.INFO)

logging.info("this is info method")
logging.critical("this is critical")
logging.exception("exception log")
logging.debug("debug log")
