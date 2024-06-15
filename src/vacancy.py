class Vacancy:
    vacancies: list = []

    def __init__(self, name, url, salary_from, salary_to, city, experience):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.city = city
        self.experience = experience
        # self.snippets = "" # нежелательно хранить None, потому что по этой строке может быть выборка в запросе
        self.validate()

    def validate(self):
        if self.salary_from is None:
            self.salary_from = 0
        else:
            self.salary_from = self.salary_from
        #
        if self.salary_to is None:
            self.salary_to = 0
        else:
            self.salary_to = self.salary_to

    def __lt__(self, other):
        if self.salary_from < other.salary_from:
            return True
        else:
            return False

    def __str__(self):
        return (f'Название: {self.name},\n'
                f'url: {self.url},\n'
                f'Зарплата: {self.salary_from} - {self.salary_to},\n'
                f'Город: {self.city},\n'
                f'Опыт: {self.experience}\n')

    @classmethod
    def create_vacancies(cls, data: list):
        """ Принимаем список словарей. С помощью цикла создаются сами вакансии"""
        instances = []
        for item in data:
            url = item.get('alternate_url')
            pass

            # instance = cls(name, salary_from, salary_to, city, experience, url)

    @staticmethod
    def cast_to_object_list(vacancies: list):
        list_vacancies = []
        for vacancy in vacancies:
            vacancy_object = Vacancy(vacancy.get("name"),
                                     vacancy.get("alternate_url"),
                                     vacancy.get("salary").get("from"),
                                     vacancy.get("salary").get("to"),
                                     vacancy.get("area").get("name"),
                                     vacancy.get("experience").get("name")
                                     )
            list_vacancies.append(vacancy_object)

        Vacancy.vacancies = list_vacancies
        return Vacancy.vacancies

    def to_dict(self):
        return {"name": self.name,
                "alternate_url": self.url,
                "salary_from": self.salary_from,
                "salary_to": self.salary_to,
                "city": self.city,
                "experience": self.experience
                }

    @staticmethod
    def add_vacancy(new_vacancy):
        return Vacancy.vacancies.append(new_vacancy)

    @staticmethod
    def delete_vacancy(del_vacancy):
        return Vacancy.vacancies.remove(del_vacancy)

    @staticmethod
    def sorted_desc_list():
        """ сортируем список """
        sort_key = lambda vac: vac
        Vacancy.vacancies.sort(key=sort_key, reverse=True)

    @staticmethod
    def top_n_list(top_n):
        Vacancy.vacancies = Vacancy.vacancies[:top_n]

    @staticmethod
    def search_by_keywords(searched_words: list):
        new_list = []
        searched_word_set = set([item.lower() for item in searched_words])
        for vacancy in Vacancy.vacancies:
            if searched_word_set.intersection(set(vacancy.name.lower().split())):
                new_list.append(vacancy)
        Vacancy.vacancies = new_list

