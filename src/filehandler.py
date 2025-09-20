import json
import os
from abc import ABC, abstractmethod
from src.vacancies import Vacancy


class FileHandler(ABC):
    """ Класс FeleHandler является абстрактным родительским классом """
    vacancies: list
    criteria: str

    @abstractmethod
    def add_vacancies(self, vacancies, vacancy_id_new) -> None:
        pass

    @abstractmethod
    def call_vacancies(self, vacansies, criteria) -> None:
        pass

    @abstractmethod
    def del_vacancies(self, vacancies, criteria) -> None:
        pass


class JSONSaver(FileHandler):
    """ Класс JSONSaver используется для добавления, получения, удаления вакансий """
    vacancies: list
    criteria: str

    def __init__(self, vacancies, criteria, path='data/vacancie.json') -> None:
        self.__vacancies = vacancies if vacancies else []
        self.criteria = criteria
        self.__full_path = os.path.abspath(path)

    def add_vacancies(self, vacancies, vacancy1) -> None:
        '''Добавление вакансий в файл'''
        for vacancy in self.__vacancies:
            n = 0
            if vacancy1.vacancy_id == vacancy.vacancy_id:
                n += 1
            if n > 0:
                self.__vacancies.append(vacancy1)
        return self.__vacancies

    def call_vacancies(self, vacancies, criteria) -> None:
        '''Получение вакансий из файла по критериям'''
        n = 0
        my_list = []
        for crit in criteria:
            for vacanc in self.__vacancies:
                if (crit.lower() in vacanc.name.lower() or crit.lower() in vacanc.description['requirement'].lower()):
                    n += 1
                    my_list.append(vacanc)
                else:
                    continue
        if n == 0:
            print("Критерии запроса не найдены")
        return my_list

    def del_vacancies(self, vacancies, criteria) -> None:
        '''Удаление вакансии из файла'''
        for vacan in self.__vacancies:
            if self.criteria in vacan.vacancy_id:
                self.__vacancies.remove(vacan)
                break
        return self.__vacancies

    def save_to_json(self, new_dict: dict, path: str) -> None:
        """Сохранение информации в json-файл"""

        with open(self.__full_path, 'w', encoding='UTF-8') as file:
            json.dump(new_dict, file, ensure_ascii=False)


vacancy1 = Vacancy("00000001", "Python Developer", "<https://hh.ru/vacancy/123456>",
                   "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

# if __name__ == "__main__":
#     hh_api = HeadHunterAPI()
#     hh_vacancies = hh_api.load_vacancies("Python")
#     vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
#     json_saver = JSONSaver(vacancies_list, "Python")
#     new_list = json_saver.add_vacancies(vacancies_list, vacancy1)
# #    del_list = json_saver.del_vacancies(vacancies_list, vacancy1)
#     vacancie = json_saver.save_to_json(my_dict, '../data/vacancie.json')
# #    print(new_list)
