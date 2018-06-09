import logging

logging.basicConfig(filename="sample.log",filemode="a",level=logging.ERROR) #debug<info<warning<error

logging.debug("debug Message")
logging.info("information")
logging.warning("i'm warning you")
logging.error("error message\n")