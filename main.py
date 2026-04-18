from src.api_hh import HeadHunterAPI
from src.vacancies import Vacancy, vacancy
from src.filehandler import JSONSaver


# Пример работы конструктора класса с одной вакансией
vacancy = Vacancy(
    "93353083",
    "Python Developer",
    "<https://hh.ru/vacancy/123456>",
    "100 000-150 000 руб.",
    "Требования: опыт работы от 3 лет...",
)
vacancy1 = Vacancy(
    "00000001",
    "Python Developer",
    "<https://hh.ru/vacancy/123457>",
    "120 000-150 000 руб.",
    "Требования: опыт работы от 3 лет...",
)

# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = ["HeadHunter"]
    print("Ввод информации для поискового запроса: ")
    key_word = input("Введите ключевое слово для поиска вакансий в API. Например, Python ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат:  Например:100000-150000 ").split("-")

# Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

# Создание экземпляра класса для выбора, добавления, удаления вакансий
    json_saver = JSONSaver()

# Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.load_vacancies(key_word)
# Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    print(vacancies_list)
# Добавление вакансий с сохранением информации о вакансиях в файл
    for vac in hh_vacancies:
        json_saver.add_vacancies(Vacancy(vac["id"], vac["name"], vac["url"], vac["salary"], vac["snippet"]))

# Фильтрация вакансий по ключевым словам
    filtered_vacancies = [Vacancy(**v) for v in json_saver.call_vacancies(filter_words)]
    print(filtered_vacancies)
# Фильтрация и сортировка вакансий по заработной плате
    ranged_vacancies = []
    salary_range[0] = int(salary_range[0])
    salary_range[1] = int(salary_range[1])
    print(salary_range[0], salary_range[1])
    for vac1 in filtered_vacancies:
        if vac1.salary >= salary_range[0] and vac1.salary <= salary_range[1]:
            ranged_vacancies.append(vac1)
    sorted_vacancies = Vacancy.sorted_by_salary(ranged_vacancies)

# Формируем список для вывода топ-вакансий
    top_vacancies = []
    n = 0
    for vacc in sorted_vacancies:
        if n <= top_n:
            top_vacancies.append(vacc)
            n += 1

    print(top_vacancies)


if __name__ == "__main__":
     user_interaction()
