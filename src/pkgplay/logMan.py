import logging
from colorlog import ColoredFormatter

def setup_logger():
    logger = logging.getLogger('my_package')
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s%(purple)s%(function)-8s%(reset) %(blue)s%(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red',
        }
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

logger = setup_logger()

def test_logger():
    logger.info('This is an info message')
    logger.error('This is an error message')

test_logger()