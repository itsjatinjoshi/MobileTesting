import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', filename="log.data", datefmt='%d/%m/%y %I:%M:%S %p %A', level= logging.DEBUG)
logging.critical("This is Critical msg.")
logging.warning("This is Warning msg.")
logging.error("This is Error msg.")
logging.info("This is Info msg.")
logging.debug("This is Debug msg.")
