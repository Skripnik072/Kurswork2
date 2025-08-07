from src.api_hh import HeadHunterAPI


class Vacancy():
    """Класс для сравнения, валидации вакансий"""
    vacancy_id: str
    name: str
    url: str
    salary: str
    description: str

    def __init__(self, vacancy_id, name, url, salary, description):
        self.vacancy_id = vacancy_id
        self.name = name
        self.url = url
        self.salary = salary
        self.description = description


    @staticmethod
    def __valid_salary(vacancies: list[dict]):
        '''Проверка указана ли зарплата'''
        for vacanc in vacancies:
            vacanc["salary"] = vacanc.get("salary", 0) or 0
        return vacancies

    @classmethod
    def cast_to_object_list(cls, vacancies):
        '''Формируем список из JSON-файла'''
        my_list = []
        my_dict = {}
        sl_vacancies = cls.__valid_salary(vacancies)
        for vacans in sl_vacancies:
            my_dict = {'vacancy_id': vacans['id'], 'name': vacans['name'], 'url': vacans['url'], 'salary': vacans['salary'],
                      'description': vacans['snippet']}

            my_list.append(cls(**my_dict))
        return my_list

    def __repr__(self):
#        return str(self.salary)
        return  (f"Vacancy(vacancy_id={self.vacancy_id}, name='{self.name}', url='{self.url}', salary={self.salary}, "
                 f"description='{self.description}')")

    @staticmethod
    def __salary_to_int(salary):
        """Метод преобразования данных по зарплате в число"""
        salary_aver = 0
        if isinstance(salary, dict):
            salary_aver = int(salary['to']) + int(salary['from']) / 2
        else:
            salary_aver = int(salary)
        return salary_aver

    def __le__(self, other):
        """Метод для сравнения вакансий по зарплате"""
        return f'{self.__salary_to_int(self.salary)} <= {self.__salary_to_int(other.salary)}'


vacancy = Vacancy("93353083", "Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.load_vacancies("Python")
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    print(vacancies_list)
