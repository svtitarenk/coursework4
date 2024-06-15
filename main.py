from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.file_explorer import FileWorker

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()


# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    input_salary = input("Введите ожидаемую зарплату для поиска вакансий: ")
    # search_query = 'Python'
    # input_salary = 100000

    # создаем экземпляр класса FileWorker и передаем название файла
    file_ex = FileWorker('vacancies.json')

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies(search_query, int(input_salary))

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    # сохранили список словарей как данные в файл vacancies
    file_ex.save_to_file(vacancies_list)
    # vacancies_dict = [Vacancy.to_dict() for vacancy in vacancies_list]
    # print(vacancies_dict)

    # реализовать выбор вакансии для сохранения или удаления
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

    Vacancy.add_vacancy(vacancy)
    # print('vacancies_list.add_vacancy(vacancy)', vacancies_list[-1].name)
    Vacancy.delete_vacancy(vacancy)
    # print('vacancies_list.delete_vacancy(vacancy)',vacancies_list[-1].name)

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    # filter_words = "Django"
    Vacancy.search_by_keywords(filter_words)
    Vacancy.sorted_desc_list()

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # top_n = 5
    top_n_list = Vacancy.top_n_list(int(top_n))
    # print(*top_n_list, sep='\n')
    print(*Vacancy.vacancies, end='\n', sep='\n')
    print('пустая строка')
    file_ex.save_to_file(Vacancy.vacancies)

    # используется в запросе API ранее для получения вакансий с указанной вилкой
    # salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
    # salary_range = 50000

    # filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    #
    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    #
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
