import logging

def log(path, multipleLocs=False):
    """
    Log to multiple locations if multipleLocs is True
    """
    logger = logging.getLogger("Test_logger")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(path)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    if multipleLocs:
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)
        logger.addHandler(console)

    logger.info("This is an informational message")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("You can't do that!")

    logger.critical("THIS IS A SHOW STOPPER!!!")

if __name__ == "__main__":
    log("sample.log") # log only to file
    log("sample2.log", multipleLocs=True) # log to file AND console!