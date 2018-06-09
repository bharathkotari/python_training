import logging

logging.basicConfig(filename="sample1.log",filemode="w",level=logging.INFO) #debug<info<warning<error
log=logging.getLogger("ex")
try:
	raise RuntimeError
except Exception:
	log.exception(" im printing error !")