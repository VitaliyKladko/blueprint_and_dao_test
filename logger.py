import logging
from config import LOGGER_PATH, LOGGER_FORMAT

def logger_config():

    """Функция загружает конфигурацию пользовательского логгера"""
    # Создаем логгер и устанавливаем уровень
    my_app_logger = logging.getLogger('my_app_logger')
    my_app_logger.setLevel(logging.DEBUG)

    # Создаем хендлер, устанавливаем его уровень и подключаем к логгеру 'my_app_logger'
    my_app_logger_handler = logging.FileHandler(LOGGER_PATH)
    my_app_logger_handler.setLevel(logging.DEBUG)
    my_app_logger.addHandler(my_app_logger_handler)

    #создаем формат для логгера и подключаем его к хендлеру
    my_app_logger_format = logging.Formatter(LOGGER_FORMAT)
    my_app_logger_handler.setFormatter(my_app_logger_format)
