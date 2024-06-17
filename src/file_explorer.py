import os
from pathlib import Path
import json
from config import ROOT_DIR
from src.hh_api import HeadHunterAPI
from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class FileManager(ABC):

    @abstractmethod
    def __init__(self, file_name, directory='data'):
        pass

    def save_to_file(self, data: list[Vacancy]):
        pass

    def open_file(self, file_path):
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

    @staticmethod
    def check_directory_exist(directory):
        """
        Функция проверяет наличие папки и файла
        возвращает True или False
        """
        directory_path = os.path.join(ROOT_DIR, directory)
        check_dir = Path(directory_path)
        if check_dir.is_dir():  # проверяем есть ли папка
            return True
        else:
            return False

    @staticmethod
    def check_file_exist(directory, file_name):
        """
        Функция проверяет наличие файла
        возвращает True или False
        """
        file_path = os.path.join(ROOT_DIR, directory, file_name)
        check_file = Path(file_path)
        try:
            my_abs_path = check_file.resolve(strict=True)
        except FileNotFoundError:
            return False


if __name__ == "__main__":
    # file = FileWorker(HeadHunterAPI.get_vacancies())
    # print(file)

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
