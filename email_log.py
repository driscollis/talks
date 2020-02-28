import logging
import logging.handlers


def log():
    """
    Log to email
    """
    logger = logging.getLogger("email_logger")
    logger.setLevel(logging.INFO)
    fh = logging.handlers.SMTPHandler('smtp.my_server.com',
                                      fromaddr='log@my_server.com',
                                      toaddrs=['mdriscoll@my_server.com'],
                                      subject='Python log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    logger.info("This is an informational message")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("You can't do that!")

    logger.critical("THIS IS A SHOW STOPPER!!!")

if __name__ == "__main__":
    log()