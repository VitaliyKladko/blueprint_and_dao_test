from flask import Flask

# Импортируем блюпринт
from app.main.views import main_blueprint
from app.candidates.views import candidates_blueprint
from app.vacancies.views import vacancies_blueprint
from logger import logger_config

# Создаем экземпляр Flask
app = Flask(__name__)
# загружаем конфиг логгера
logger_config()

# Регистрируем первый блюпринт (main_blueprint, candidates_blueprint, vacancies_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(candidates_blueprint)
app.register_blueprint(vacancies_blueprint)

# Запускаем сервер, только если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run()