import logging
import os
from datetime import datetime
from logging import Logger


def get_logger() -> Logger:
    """
    Функция создает экземпляр класса Logger.\n
    Папка и файл для записи логов создаются автоматически.\n
    Формат вывода: datetime: level: message.

    :return: экземпляр класса Logger
    """

    fmt = '%(asctime)s-%(msecs)03d: %(levelname)s: %(message)s'
    datefmt = '%d-%m-%y %H-%M-%S'
    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)

    if not os.path.exists('logs'):
        os.makedirs('logs')

    dt = datetime.now().strftime('%m-%d-%y-%H-%M-%S-%f')
    file_name = f'logs/logs-{dt}.txt'
    handler = logging.FileHandler(file_name)
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger


logger = get_logger()
logger.debug('qwerty')
logger.info('qwerty')
