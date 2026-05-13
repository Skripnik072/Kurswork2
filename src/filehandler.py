import json
import os
from abc import ABC, abstractmethod
from typing import Optional, Any
from src.vacancies import Vacancy


class FileHandler(ABC):
    """ Класс FeleHandler является абстрактным родительским классом """
    vacancies: list
    filter_words: Optional[str]

    @abstractmethod
    def add_vacancies(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def call_vacancies(self, filter_words: Optional[str]) -> None:
        pass

    @abstractmethod
    def del_vacancies(self, vacancy: Vacancy) -> None:
        pass


class JSONSaver(FileHandler):
    """ Класс JSONSaver используется для добавления, получения, удаления вакансий """
    vacancies: list
    filter_words: Optional[str]

    def __init__(self, path: str ='data/vacancie.json') -> None:
        self.__vacancies: list[Vacancy] = []
        self.__full_path = os.path.abspath(path)
        if not os.path.exists(self.__full_path):
            with open(self.__full_path, "w", encoding="UTF-8") as file:
                json.dump([], file, ensure_ascii=False, indent=4)

    def __save_to_json(self, new_dict: list[dict]) -> None:
        """Сохранение информации в json-файл"""

        with open(self.__full_path, 'w', encoding='UTF-8') as file:
            json.dump(new_dict, file, ensure_ascii=False, indent=4)

    def add_vacancies(self, vacancy: Vacancy) -> None:
        '''Добавление вакансий в файл'''
        if self.__vacancies:
            self.__vacancies = [
                Vacancy(v["vacancy_id"], v["name"], v["url"], v["salary"], v["description"])
                for v in self.call_vacancies()
            ]
        if vacancy not in self.__vacancies:
            self.__vacancies.append(vacancy)
        new_list = [vacancy.to_dict(vacancy) for vacancy in self.__vacancies]
        self.__save_to_json(new_list)

    def call_vacancies(self, filter_words: Optional[str] = None) -> Any:
        '''Получение вакансий из файла по критериям'''
        with open(self.__full_path, "r", encoding="UTF-8") as file:
            data = json.load(file)
            nom_vac = 0
            if filter_words:
                return [vacancy for vacancy in data if all(word in vacancy["name"].lower() for word in filter_words)]
            nom_vac += 1
            if nom_vac == 0:
                print("Критерии запроса не найдены")
            return data

    def del_vacancies(self, vacancy: Vacancy) -> None:
        """Удаление вакансии из файла"""
        if self.__vacancies:
            self.__vacancies = [
                Vacancy(v["vacancy_id"], v["name"], v["url"], v["salary"], v["description"])
                for v in self.call_vacancies()
            ]
        if vacancy in self.__vacancies:
            self.__vacancies.remove(vacancy)
        new_list = [vacancy.to_dict(vacancy) for vacancy in self.__vacancies]
        self.__save_to_json(new_list)


vacancy1 = Vacancy("00000001", "Python Developer", "<https://hh.ru/vacancy/123456>",
                   "100000-150000", "Требования: опыт работы от 3 лет...")

# if __name__ == "__main__":
#     hh_api = HeadHunterAPI()
#     hh_vacancies = hh_api.load_vacancies("Python")
#     vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
#     json_saver = JSONSaver(vacancies_list, "Python")

#     new_list = json_saver.add_vacancies(vacancies_list, vacancy1)
#     del_list = json_saver.del_vacancies(vacancies_list, vacancy1)
#     vacancie = json_saver.save_to_json(my_dict, '../data/vacancie.json')
#     print(new_list)
