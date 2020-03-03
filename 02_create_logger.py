import logging

logging.basicConfig(filename="ex_logger.log")
log = logging.getLogger("ex")
log.setLevel(logging.INFO)

try:
    raise RuntimeError
except Exception as err:
    log.exception("Error!")