from src.filehandler import JSONSaver
from src.vacancies import Vacancy


def test_filehand_init(jsonsaver1):
    assert jsonsaver1._JSONSaver__full_path == 'C:\\Users\\it-pc.ru\\PycharmProjects\\PythonPKW2\\tests\\data\\vacancie.json'


def test_call_vacancies(vacancy_dubl):
    json_saver = JSONSaver("Developer")
    assert json_saver.call_vacancies("Developer") == [
        Vacancy(
            vacancy_id="93353072",
            name="Developer",
            url="<https://hh.ru/vacancy/456789>",
            salary=130000,
            description="Требования: опыт работы от 3 лет...")
    ]
