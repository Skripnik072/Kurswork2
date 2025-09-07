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
    vacancy = Vacancy.cast_to_object_list(hh_vacanc)[0]
    assert vacancy.vacancy_id == "93353083"
    assert vacancy.name == "Тестировщик комфорта квартир"
    assert vacancy.url == "https://api.hh.ru/vacancies/93353083?host=hh.ru"
    assert vacancy.salary == 120000
    assert vacancy.description == {"requirement": "Занимать активную жизненную позицию"}


def test_sorted_by_salary(sort_salary):
    vacancy = Vacancy.sorted_by_salary(sort_salary)[0]
    vacancy1 = Vacancy.sorted_by_salary(sort_salary)[1]
    assert vacancy.vacancy_id ==93353083
    assert vacancy1.vacancy_id ==93353082
