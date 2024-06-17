import json

import requests
from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def get_vacancies(self, keyword=None):
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '',
                       'salary': 0,
                       'currency': 'RUR',
                       'page': 0,
                       'per_page': 100,
                       'only_with_salary': True}
        self.vacancies = []
        # super().__init__(file_worker)

    def get_vacancies(self, keyword, salary):
        self.params['text'] = keyword
        self.params['salary'] = salary
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            if not vacancies:
                break
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

        return self.vacancies

    # def __repr__(self):
    #     for vacancy in self.vacancies:
    #         return f"{vacancy["alternate_url"]}"


if __name__ == "__main__":
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    hh_vacancies = json.dumps(hh_api.get_vacancies('Python'), ensure_ascii=False, indent=4)
    print(hh_vacancies)

