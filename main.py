from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.file_explorer import FileWorker

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")


#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
#
#     filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
#
#     ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
#
#     sorted_vacancies = sort_vacancies(ranged_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)

# input()

file_ex = FileWorker('vacancies.json')

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies("Python", 100000)

# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
# print(vacancies_list[0].name)

# сохранили список словарей как данные в файл vacancies
file_ex.save_to_file(vacancies_list)
# vacancies_dict = [Vacancy.to_dict() for vacancy in vacancies_list]
# print(vacancies_dict)

# Пример работы контструктора класса с одной вакансией
vacancy = Vacancy(
                 "Test1",
                 "https://hh.ru/vacancy/96169741_1241",
                 1500,
                 "",
                 "Test_Сербия",
                 "От 3 до 6 лет"
                )

# Сохранение информации о вакансиях в файл

file_ex.add_vacancy(vacancy)
file_ex.delete_vacancy(vacancy)


if __name__ == "__main__":
    user_interaction()