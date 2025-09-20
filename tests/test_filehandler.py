from src.filehandler import JSONSaver
from src.vacancies import Vacancy


def test_filehand_init(jsonsaver1):
    assert jsonsaver1.criteria == "Python Developer"
    assert jsonsaver1._JSONSaver__full_path == 'C:\\Users\\it-pc.ru\\PycharmProjects\\PythonPKW2\\tests\\data\\vacancie.json'
    assert jsonsaver1._JSONSaver__vacancies == []


def test_add_vacancies(vacancy_dubl, vacancy1):
    json_saver = JSONSaver(vacancy_dubl, "Python")
    assert json_saver.add_vacancies([vacancy_dubl], vacancy1) == [
            Vacancy(
                vacancy_id="93353081",
                name="Python Devel",
                url="<https://hh.ru/vacancy/123456>",
                salary=120000,
                description="Требования: опыт работы от 3 лет..."),
            Vacancy(
                vacancy_id="93353072",
                name="Developer",
                url="<https://hh.ru/vacancy/456789>",
                salary=120000,
                description="Требования: опыт работы от 3 лет..."),
            Vacancy(
                vacancy_id="93353083",
                name="Python Developer",
                url="<https://hh.ru/vacancy/123456>",
                salary=120000,
                description="Требования: опыт работы от 3 лет..."),
    ]


def test_call_vacancies(vacancy_dubl, vacancy1):
    json_saver = JSONSaver(vacancy_dubl, "Python")
    assert json_saver.call_vacancies([vacancy_dubl], "Developer") == [
        Vacancy(
            vacancy_id="93353072",
            name="Developer",
            url="<https://hh.ru/vacancy/456789>",
            salary=130000,
            description="Требования: опыт работы от 3 лет...")
    ]
