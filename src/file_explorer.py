import os
from pathlib import Path
import json
from config import ROOT_DIR
from src.hh_api import HeadHunterAPI
from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class FileManager(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def save_data(self, data):
        pass


class FileWorker(FileManager):

    def __init__(self, file_name, directory='data'):
        # Открываем файл по составному пути из конфига, проверяем есть ли папка и файл
        self.directory = directory
        self.file_name = file_name
        self.file_path = os.path.join(ROOT_DIR, self.directory, self.file_name)
        if not self.check_directory_exist(directory):
            os.mkdir('data')
            self.directory = directory
        else:
            self.directory = directory

        if not self.check_file_exist(directory, file_name):
            checked_path = os.path.join(ROOT_DIR, directory, file_name)
            with open(checked_path, 'w', encoding='utf-8') as f:
                f.write('[]')
            self.file_name = file_name
            self.file_path = checked_path
        else:
            self.file_name = file_name


    def save_to_file(self, data: list[Vacancy]):
        """
        :param data: передаем список экземпляров вакансий
        :return: список словарей json с вакансиями
        """
        list_to_write = []
        with open(self.file_path, 'w', encoding='utf-8') as file:
            for row in data:
                row_in_dict = row.to_dict()
                list_to_write.append(row_in_dict)
            json.dump(list_to_write, file, ensure_ascii=False, indent=4)

    def open_file(self, file_path):
        self.file_path = file_path
        with open(file_path, 'r', encoding='utf-8') as file:
            list_of_dict = file.read()
            return list_of_dict

    # def read_data(self):
    #     """" открываем файл """
    #     with open(self.file_path, 'r', encoding='utf-8') as file:
    #         content = json.load(file)
    #         vacancies: list[Vacancy] = []
    #         for row in content:
    #             vacancy = Vacancy(
    #                             row["name"],
    #                             row["alternate_url"],
    #                             row["salary_from"],
    #                             row["salary_to"],
    #                             row["city"],
    #                             row["experience"]
    #                             )
    #             vacancies.append(vacancy)
    #     return vacancies

    # def add_vacancy(self, vacancy):
    #     """
    #     Добавление одной вакансии в файл
    #     """
    #     vacancies = self.read_data()
    #     print(vacancies[-1])
    #     vacancies.append(vacancy)
    #     self.save_to_file(vacancies)
    #
    # def delete_vacancy(self, vacancy):
    #     '''
    #     Функция удаляет отобранную по критериям вакансию и сохраняет изменения в файл
    #     '''
    #     vacancies = self.read_data()
    #     print('vacancies[-1].name', vacancies[-1].name)
    #     print('vacancy.name', vacancy.name)
    #     lookup_object = [item for item in vacancies if vacancy.url == item.url][0]
    #     vacancies.remove(lookup_object)
    #     self.save_to_file(vacancies)

    @staticmethod
    def check_directory_exist(directory):
        """
        Функция проверяет наличие папки и файла
        возвращает True или False
        """
        directory_path = os.path.join(ROOT_DIR, directory)
        check_dir = Path(directory_path)
        try:
            check_dir.is_dir()  # проверяем есть ли папка
            return True
        except FileNotFoundError:
            return False

    @staticmethod
    def check_file_exist(directory, file_name):
        """
        Функция проверяет наличие файла
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



# students_json = json.dumps(students_dict_list, indent=4)
# Сохранение JSON в файл
# with open("students.json", "w") as file:
#     file.write(students_json)


if __name__ == "__main__":
    # file = FileWorker(HeadHunterAPI.get_vacancies())
    # print(file)

    # class Student:
    #     def __init__(self, name, age):
    #         self.name = name
    #         self.age = age
    #
    #     def to_dict(self):
    #         return {"name": self.name, "age": self.age}
    #
    #
    # students = [Student(name="Alice", age=20), Student(name="Bob", age=22), Student(name="Charlie", age=23)]
    # students_dict_list = [student.to_dict() for student in students]




    file_ex = FileWorker('vacancies.json')

    # Получение вакансий с hh.ru в формате JSON
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies('Python')
    print(hh_vacancies)

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    # print(vacancies_list[0].name)

    file_ex.save_to_file(vacancies_list)
    # vacancies_dict = [Vacancy.to_dict() for vacancy in vacancies_list]
    # print(vacancies_dict)

