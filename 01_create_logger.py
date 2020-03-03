import logging

logging.basicConfig(filename="ex_logger.log", level=logging.INFO)
log = logging.getLogger("ex")

try:
    raise RuntimeError
except Exception as err:
    log.exception("Error!")