import logging
import colorlog
import os
# from libFuncs.func_test import things


def make_logger(logFilepath='pkgPlay.log', loggerName=__name__, logLevel="WARNING"):
    """Log plain text to file and terminal with colors"""
    
    # create log folder
    if not os.path.exists('logs'):
        os.mkdir('logs')
    logFilepath = os.path.join(os.getcwd(), 'logs', f'{loggerName}.log')
    l = logging.getLogger(loggerName)

    # log to file
    logfile_handler = logging.FileHandler(logFilepath)
    plain_formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(filename)s:%(lineno)d:%(module)s:%(funcName)s) - %(message)s')
    logfile_handler.setFormatter(plain_formatter)

    match logLevel.upper():
        case "CRITICAL":
            logfile_handler.setLevel(logging.CRITICAL)
        case "ERROR":
            logfile_handler.setLevel(logging.ERROR)
        case "WARNING":
            logfile_handler.setLevel(logging.WARNING)
        case "INFO":
            logfile_handler.setLevel(logging.INFO)
        case "DEBUG":
            logfile_handler.setLevel(logging.DEBUG)
        case "NOTSET":
            logfile_handler.setLevel(logging.NOTSET)
        case _:
            logfile_handler.setLevel(logging.WARNING)
    
    # Logging info level to stdout with colors
    terminal_handler = colorlog.StreamHandler()
    color_formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s - 8s(reset)s %(asctime)s - %(purple)s(%(filename)s:%(lineno)d:%(module)s:%(funcName)s)%(reset)s - %(blue)s%(message)s',
        datefmt=None,
        reset=True,
        log_colors={
            "CRITICAL": 'red,bg_white',
            "ERROR":    'red',
            "WARNING":  'yellow',
            "INFO":     'green',
            "DEBUG":    'cyan'
        },
        secondary_log_colors={},
        style='%'
    )

    match logLevel.upper():
        case "CRITICAL":
           l.setLevel(logging.CRITICAL)
        case "ERROR":
            l.setLevel(logging.ERROR)
        case "WARNING":
            l.setLevel(logging.WARNING)
        case "INFO":
            l.setLevel(logging.INFO)
        case "DEBUG":
            l.setLevel(logging.DEBUG)
        case "NOTSET":
            l.setLevel(logging.NOTSET)
        case _:
            l.setLevel(logging.WARNING)
    
    terminal_handler.setFormatter(color_formatter)

    # add handlers to logger
    l.addHandler(logfile_handler)
    l.addHandler(terminal_handler)

    return l
if __name__ == '__main__':
    logger = make_logger(logLevel='DEBUG')
    
    logger.critical('critical')
    logger.error('error')
    logger.warning('warning')
    logger.info('informational')
    logger.debug('degub')
    
    print("all done")
    