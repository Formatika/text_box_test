import logging


def gen_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        logger.propagate = 0
        console = logging.StreamHandler()
        logger.addHandler(console)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s  - %(message)s'
        )
        console.setFormatter(formatter)
    return logger
