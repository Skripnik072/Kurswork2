import statistics
from decimal import Decimal
from fractions import Fraction
from typing import Any


class Vacancy:
    """Класс для сравнения, валидации вакансий"""

    __slots__ = ["vacancy_id", "name", "url", "salary", "description"]
    vacancy_id: str
    name: str
    url: str
    salary: str
    description: str

    def __init__(self, vacancy_id, name, url, salary, description) -> None:
        self.vacancy_id = vacancy_id
        self.name = name
        self.url = url
        self.salary = self.__valid_salary(salary)
        self.description = description

    @staticmethod
    def __valid_salary(salary: dict[str]) -> None | int | float | Decimal | Fraction | Any:
        """Проверка указана ли зарплата"""
        if isinstance(salary, dict):
            if salary:
                if salary.get("from") and salary.get("to"):
                    return statistics.mean([salary.get("from"), salary.get("to")])
                elif salary.get("from") or salary.get("to"):
                    if salary.get("from"):
                        return salary.get("from")
                    else:
                        return salary.get("to")
                else:
                    return 0
        elif isinstance(salary, str):
            list = salary.split(" - ")
            for i in list:
                my_string = i[:3] + i[4:7]
            salar = (int(my_string[0]) + int(my_string[1])) / 2
            return salar
        else:
            return 0

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict]) -> list:
        """Формируем список из списка словарей"""
        my_list = []

        for vacans in vacancies:
            my_list.append(cls(vacans["id"], vacans["name"], vacans["url"], vacans["salary"], vacans["snippet"]))

        return my_list

    def __repr__(self) -> str:
        """Формируем список экземпляров класса"""
        return (
            f"Vacancy(vacancy_id={self.vacancy_id}, name='{self.name}', url='{self.url}', salary={self.salary}, "
            f"description='{self.description}')"
        )

    def __lt__(self, other) -> None:
        return self.salary < other.salary

    def __gt__(self, other) -> None:
        return self.salary > other.salary

    @staticmethod
    def sorted_by_salary(my_list: list) -> list:
        """Метод сортировки вакансий по зарплате"""
        ranged_vacancies = sorted(my_list, key=lambda x: x.salary, reverse=True)
        return ranged_vacancies

    def to_dict(self, vacancy) -> dict:
        """Метод перевода экземпляра класса в словарь"""
        my_dict = {
            "vacancy_id": vacancy.vacancy_id,
            "name": vacancy.name,
            "url": vacancy.url,
            "salary": vacancy.salary,
            "description": vacancy.description,
        }
        return my_dict


vacancy = Vacancy(
    "93353083",
    "Python Developer",
    "<https://hh.ru/vacancy/123456>",
    "100 000-150 000 руб.",
    "Требования: опыт работы от 3 лет...",
)


# if __name__ == "__main__":
#     hh_api = HeadHunterAPI()
#     hh_vacancies = hh_api.load_vacancies("Python")
#     vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
#     print(vacancies_list)
# m_list = []
# for vac in vacancies_list:
#     m_dict = vacancy.to_dict(vac)
#     m_list.append(m_dict)
# my_dict = {'item': m_list}
# print(my_dict)
