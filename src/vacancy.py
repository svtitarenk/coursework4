class Vacancy:
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
        if self.salary_from is None:
            self.salary_from = 0
        else:
            self.salary_to = self.salary_to

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

        return list_vacancies

    def to_dict(self):
        return {"name": self.name,
                "alternate_url": self.url,
                "salary_from": self.salary_from,
                "salary_to": self.salary_to,
                "city": self.city,
                "experience": self.experience
                }



