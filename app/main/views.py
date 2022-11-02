from flask import Blueprint
import logging

main_blueprint = Blueprint('main_blueprint', __name__)

# подключаем логгер
my_app_logger = logging.getLogger('my_app_logger')

@main_blueprint.route('/')
def page_index():
    # Устанавливаем логгер на вьюху
    my_app_logger.debug('Открытие главной стр.')
    return 'Это главная страница'