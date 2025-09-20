import pytest

from src.vacancies import Vacancy
from src.api_hh import HeadHunterAPI
from src.filehandler import JSONSaver

@pytest.fixture
def vacancies():
    return {"items":[{"id":"93353083","premium":'false'}]}

@pytest.fixture
def vacancy1():
    return Vacancy(
        vacancy_id = "93353083",
        name = "Python Developer",
        url = "<https://hh.ru/vacancy/123456>",
        salary = {"from": 100000, "to": 140000},
        description = "Требования: опыт работы от 3 лет...")

@pytest.fixture
def vacancy2():
    return Vacancy(
        vacancy_id = "93353072",
        name = "Developer",
        url = "<https://hh.ru/vacancy/456789>",
        salary = {"from": 120000, "to": 140000},
        description = "Требования: опыт работы от 3 лет...")

@pytest.fixture
def vacancy_dubl():
    return [
        Vacancy(
        vacancy_id = "93353081",
        name = "Python Devel",
        url = "<https://hh.ru/vacancy/123456>",
        salary = {"from": 100000, "to": 140000},
        description = "Требования: опыт работы от 3 лет..."),
        Vacancy(
            vacancy_id="93353072",
            name="Developer",
            url="<https://hh.ru/vacancy/456789>",
            salary={"from": 100000, "to": 140000},
            description="Требования: опыт работы от 3 лет...")
        ]

@pytest.fixture
def jsonsaver1():
    return JSONSaver(
        vacancies = [],
        criteria = "Python Developer",
        path='data/vacancie.json')

@pytest.fixture
def salary1():
    return {"from": 100000, "to": 140000}

@pytest.fixture
def hh_vacanc():
    return [
    {"id":"93353083",
    "name":"Тестировщик комфорта квартир",
    "salary": {"from": 100000, "to": 140000},
    "published_at":"2024-02-16T14:58:28+0300",
    "created_at":"2024-02-16T14:58:28+0300",
    "url":"https://api.hh.ru/vacancies/93353083?host=hh.ru",
    "alternate_url":"https://hh.ru/vacancy/93353083",
    "snippet":{"requirement":"Занимать активную жизненную позицию"}}
    ]

@pytest.fixture
def sort_salary():
    return [
        Vacancy(vacancy_id=93353083,
                name='Тестировщик комфорта квартир',
                url='https://api.hh.ru/vacancies/93353083?host=hh.ru',
                salary=100000,
                description={'requirement': 'Занимать активную жизненную позицию'}),
        Vacancy(vacancy_id=93353082,
                name='Проектировщик комфорта квартир',
                url='https://api.hh.ru/vacancies/93353082?host=hh.ru',
                salary=110000,
                description={'requirement': 'Занимать активную жизненную позицию'})
    ]