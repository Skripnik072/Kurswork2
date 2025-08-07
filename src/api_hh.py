import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Класс Parser является абстрактным родительским классом
    """
    @abstractmethod
    def load_vacancies(self, keyword):
        pass

    @abstractmethod
    def connect_to_api(self):
        pass

class HeadHunterAPI(Parser):
    """
    Класс для получения вакансий с API HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def connect_to_api(self):
        """Метод подключения к API"""
        response = requests.get(self.url, headers=self.headers, params=self.params)
        status = response.status_code
        if status == 200:
            return response
        else:
            return 'Ошибка при обращении к API - error'

    def load_vacancies(self, keyword):
        """Метод для получения списка вакансий из API"""
        self.params['text'] = keyword
        while self.params.get('page') != 1:
            response = self.connect_to_api()
            vacancies = response.json().get('items', [])
#            print(vacancies)
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return vacancies


if __name__ == "__main__":
      hh_api = HeadHunterAPI()
      api_vacans = hh_api.load_vacancies("Python")
      print(api_vacans)
