import os
from config import ROOT_DIR
from pathlib import Path

file_path = os.path.join(ROOT_DIR, 'data', 'operations.json')


# response = requests.get(self.url, headers=self.headers, params=self.params)
# vacancies = response.json()['items']


def test_check_directory_exist(directory):
    """
    Функция проверяет наличие папки и файла
    возвращает True или False
    """

    directory_path = os.path.join(ROOT_DIR, directory)
    check_dir = Path(directory_path)
    try:
        check_dir.is_dir()
        return True
    except FileNotFoundError:
        return False


def check_file_exist(directory, file_name):
    """
    Функция проверяет наличие папки и файла
    возвращает True или False
    """
    file_path = os.path.join(ROOT_DIR, directory, file_name)
    check_file = Path(file_path)
    # try:
    #     check_file.exists()  # проверяем есть ли папка
    #     return True
    # except FileNotFoundError:
    #     return False
    try:
        my_abs_path = check_file.resolve(strict=True)
    except FileNotFoundError:
        return False
    else:
        create_empty_file(directory, file_name)
    # doesn't exist

def create_empty_file(directory, file_name):
    path = os.path.join(ROOT_DIR, directory, file_name)
    with open(path, 'a', encoding='utf-8') as f:
        f.write('[]')


def open_file(file_path_test):
    with open (file_path_test, 'r', encoding='utf-8') as file:
        list_of_dict = file.read()
        return list_of_dict






# def delete_vacancy(4):
#     '''
#     Функция удаляет отобранную по критериям вакансию и сохраняет изменения в файл
#     '''
#     vacancies = read_data()
#     print(vacancies)
#     for item in vacancies:
#         if vacancy == item:
#             print("vacancy exists")
#         else:
#             print(" none")
#     vacancies.remove(vacancy)


if __name__ == "__main__":
    # directory_check = test_check_directory_exist('data')
    # print('directory_check', directory_check)
    #
    # file_path = os.path.join(ROOT_DIR, 'data')
    # file_path2 = os.path.join(ROOT_DIR, 'data', 'test.json')
    # my_file = Path(file_path)
    # my_file2 = Path(file_path2)
    # print(my_file.is_dir())
    # print('my_file2.is_file()', my_file2.is_file())

    # проверяем метод проверки существования файла
    # if check_file_exist('data', 'vacancies.json') is False:
    #     create_empty_file('data', 'vacancies.json')
    # else:
    #     print("File exists")


    # проверка открытия файла и получение контента
    # file_path4 = os.path.join(ROOT_DIR, 'data', 'vacancies.json')
    # content = open_file(file_path4)
    # print(content)

    test_data = [1, 2, 3]
    test_data
    print(test_data)
