import logging


def get_logger(name: str = None) -> logging.Logger:
    """
    Returns logger object to log messages
    :param name: Logger name - set this only if separate log file is needed
    :return:
    """
    return logging.getLogger(name or 'yirmiyahu-library')
