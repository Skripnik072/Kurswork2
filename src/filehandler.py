from abc import ABC, abstractmethod
from src.vacancies import Vacancy


class FileHandler(ABC):
    """ Класс FeleHandler является абстрактным родительским классом """
    vacancies: list
    criteria: str

    def __init__(self, vacancies, criteria):
        self.__vacancies = vacancies if vacancies else []
        self.criteria = criteria

    @abstractmethod
    def add_vacancies(self, vacancies, vacancy_id_new):
        pass

    @abstractmethod
    def call_vacancies(self, vacansies, criteria):
        pass

    @abstractmethod
    def del_vacancies(self, vacancies, criteria):
        pass

class JSONSaver(FileHandler):
    """ Класс JSONSaver используется для добавления, получения, удаления вакансий """
    vacancies: list
    criteria: str

    def __init__(self, vacancies, criteria):
        self.__vacancies = vacancies if vacancies else []
        self.criteria = criteria

    def add_vacancies(self, vacancies, vacancy1):
        '''Добавление вакансий в файл'''
        for vacancy in self.__vacancies:
            n = 0
            if vacancy1['id'] == vacancy[id]:
                n += 1
            if n > 0:
                self.__vacancies.append(vacancy1)
        return self.__vacancies

    def call_vacancies(self, vacancies, criteria):
        '''Получение вакансий из файла по критериям'''
        for vacanc in self.__vacancies:
            if self.criteria in vacanc['name']:
                print (f"Вакансия по запросу {vacanc[id]}/n, {vacanc['name']}'/n, url='{vacanc['url']}'/n, "
                       f"{vacanc['salary']}/n, {vacanc['snippet']}')")
            elif self.criteria in vacanc['snippet']:
                print (f"Вакансия по запросу {vacanc[id]}/n, {vacanc['name']}'/n, url='{vacanc['url']}'/n, "
                       f"{vacanc['salary']}/n, {vacanc['snippet']}')")
            else:
                print("Критерии запроса не найдены")


    def del_vacancies(self, vacancies, criteria):
        '''Удаление вакансии из файла'''
        for vacan in self.__vacancies:
            if self.criteria in vacan['id']:
                self.__vacancies.remove(vacan)
                break
        return self.__vacancies

vacancy1 = Vacancy("00000001", "Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

if __name__ == "__main__":
    json_saver = JSONSaver()
    json_saver.add_vacancies(vacancies, vacancy1)
#    json_saver.del_vacancies(vacancy)