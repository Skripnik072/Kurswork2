from src.api_hh import HeadHunterAPI
from src.vacancies import Vacancy, vacancy
from src.filehandler import JSONSaver


# Создание экземпляра класса для работы с API сайтов с вакансиями
# hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
# hh_vacancies = hh_api.load_vacancies("Python")

# Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
# print(vacancies_list)
# list_vacancies = []
# for i in hh_vacancies:
#     list_vacancies.append(Vacancy(i["id"], i["name"], i["url"], i["salary"], i["snippet"]))

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

# Сохранение информации о вакансиях в файл
# json_saver = JSONSaver(vacancies_list, "Python")
# add_list = json_saver.add_vacancies(vacancies_list, vacancy1)
# del_list = json_saver.del_vacancies(vacancies_list, vacancy1)

# Преобразование списка экземпляров класса в словарь для передачи в JSON
# m_list = []
# for vac in add_list:
#     m_dict = vacancy.to_dict(vac)
#     m_list.append(m_dict)
# my_dict = {"item": m_list}
# vacancie = json_saver.save_to_json(my_dict, "../PythonPKW2/data/vacancie.json")
# print(m_list)

# Фильтрция списка вакансий по ключевым словам
# filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
# filtered_vacancies = json_saver.call_vacancies(m_list, filter_words)
# print(filtered_vacancies)

# Сортировка списка вакансий по уровню заработной платы
# salary_range = input("Введите диапазон зарплат: ").split(" - ")  # Пример: 100000 - 150000
# print(salary_range[0])
# print(salary_range[1])

# Отфильтровываем список по заданному критерию
# new_list = []
# for vac1 in filtered_vacancies:
#     if vac1.salary >= int(salary_range[0]) and vac1.salary <= int(salary_range[1]):
#         new_list.append(vac1)

# Сортируем список по заработной плате
# sorted_vacancies = Vacancy.sorted_by_salary(new_list)
# print(sorted_vacancies)

# Формируем список для вывода топ-вакансий
# top_n = int(input("Введите количество вакансий для вывода в топ N: "))
# vac_list = []
# n = 0
# for vacc in sorted_vacancies:
#     if n <= top_n:
#         vac_list.append(vacc)
#         n += 1
# print(vac_list)


# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = ["HeadHunter"]
    print("Ввод информации для поискового запроса: ")
    key_word = input("Введите ключевое слово для поиска вакансий в API. Например, Python ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат:  Например: 100000 - 150000 ").split(" - ")

    hh_api = HeadHunterAPI()

    hh_vacancies = hh_api.load_vacancies(key_word)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    json_saver = JSONSaver(vacancies_list, key_word)
    add_list = json_saver.add_vacancies(vacancies_list, vacancy1)
    print(add_list)
    filtered_vacancies = json_saver.call_vacancies(vacancies_list, filter_words)

    ranged_vacancies = []
    for vac1 in filtered_vacancies:
        if vac1.salary >= int(salary_range[0]) and vac1.salary <= int(salary_range[1]):
            ranged_vacancies.append(vac1)
    sorted_vacancies = Vacancy.sorted_by_salary(ranged_vacancies)

    top_vacancies = []
    n = 0
    for vacc in sorted_vacancies:
        if n <= top_n:
            top_vacancies.append(vacc)
            n += 1

    print(top_vacancies)


if __name__ == "__main__":
     user_interaction()
