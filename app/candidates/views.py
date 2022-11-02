from flask import Blueprint, render_template
import logging
from .dao.candidates_dao import CandidateDAO

# Создаем блупринт
candidates_blueprint = Blueprint('candidates_blueprint', __name__, template_folder="templates")

# Cоздаем DAO
candidates_dao = CandidateDAO('./data/candidates.json')

# подключаем логгер
my_app_logger = logging.getLogger('my_app_logger')


# Создаем вьюшку для кандидатов
@candidates_blueprint.route('/candidates/')
def page_candidates():
    candidates = candidates_dao.get_all()
    # Устанавливаем логгер
    my_app_logger.debug('Открытие страницы candidates_index.html')
    return render_template('candidates_index.html', candidates=candidates)


@candidates_blueprint.route('/candidates/<int:pk>/')
def page_candidate_all(pk):
    candidate = candidates_dao.get_by_pk(pk)
    # Устанавливаем логгер
    my_app_logger.debug(f'Открытие страницы candidates_single.html{pk}')
    return render_template('candidates_single.html', candidate=candidate)
