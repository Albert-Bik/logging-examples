import logging
import os
from datetime import datetime


def config_logging() -> None:
    """
    Функция для настройки logging.\n
    Папка и файл для записи логов создаются автоматически.\n
    Формат вывода: datetime: level: message.

    :return: None
    """

    if not os.path.exists('logs'):
        os.makedirs('logs')

    dt = datetime.now().strftime('%m-%d-%y-%H-%M-%S-%f')
    file_name = f'logs/logs-{dt}.txt'

    fmt = '%(asctime)s-%(msecs)03d: %(levelname)s: %(message)s'
    datefmt = '%d-%m-%y %H-%M-%S'
    level = logging.INFO

    logging.basicConfig(filename=file_name, format=fmt, datefmt=datefmt, level=level)


config_logging()
logging.debug('qwerty')
logging.info('qwerty')
