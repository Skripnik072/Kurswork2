from src.vacancies import Vacancy
from src.vacancies import vacancy
# from src.vacancies import cast_to_object_list
# from src.vacancies import to_list
# from src.vacancies import sorted_by_salary


def test_vacancy_init(vacancy1):
    assert vacancy1.vacancy_id == "93353083"
    assert vacancy1.name == "Python Developer"
    assert vacancy1.url == "<https://hh.ru/vacancy/123456>"
    assert vacancy1.salary == 120000
    assert vacancy1.description == "Требования: опыт работы от 3 лет..."


def test_valid_salary(salary1):
    assert vacancy._Vacancy__valid_salary(salary1) == 120000


def test_to_dict(vacancy1):
    assert vacancy.to_dict(vacancy1) ==  {"vacancy_id": "93353083",
        "name": "Python Developer",
        "url": "<https://hh.ru/vacancy/123456>",
        "salary": 120000,
        "description": "Требования: опыт работы от 3 лет..."}


def test_cast_to_object_list(hh_vacanc):
    assert Vacancy.cast_to_object_list(hh_vacanc) == [
        Vacancy(vacancy_id = 93353083,
                name = 'Тестировщик комфорта квартир',
                url = 'https://api.hh.ru/vacancies/93353083?host=hh.ru',
                salary = 120000,
                description = {'requirement': 'Занимать активную жизненную позицию'})]


def test_sorted_by_salary(sort_salary):
    assert vacancy.sorted_by_salary(sort_salary) == [
        Vacancy(vacancy_id=93353082,
                name='Проектировщик комфорта квартир',
                url='https://api.hh.ru/vacancies/93353082?host=hh.ru',
                salary=110000,
                description={'requirement': 'Занимать активную жизненную позицию'}),
        Vacancy(vacancy_id=93353083,
                name='Тестировщик комфорта квартир',
                url='https://api.hh.ru/vacancies/93353083?host=hh.ru',
                salary=100000,
                description={'requirement': 'Занимать активную жизненную позицию'})
    ]
