import logging
logging.basicConfig(level=logging.DEBUG)

def things(**kwargs):
    logging.info('THINGS(): doing my thing')
    logger = logging.getLogger()
    logger.info('THINGS(): doing it again')
