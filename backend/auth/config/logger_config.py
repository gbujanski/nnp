import logging

def setupLogger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        logger.info("Logger is configured and ready to log messages.")

    return logger
