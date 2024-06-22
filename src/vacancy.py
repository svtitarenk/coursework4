class Vacancy:
    vacancies: list = []

    def __init__(self, name, url, salary_from, salary_to, city, experience):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.city = city
        self.experience = experience
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
    def cast_to_object_list(cls, vacancies: list):
        list_vacancies = []
        for vacancy in vacancies:
            vacancy_object = cls(vacancy.get("name"),
                                 vacancy.get("alternate_url"),
                                 vacancy.get("salary").get("from"),
                                 vacancy.get("salary").get("to"),
                                 vacancy.get("area").get("name"),
                                 vacancy.get("experience").get("name")
                                 )
            list_vacancies.append(vacancy_object)

        cls.vacancies = list_vacancies
        return cls.vacancies

    @classmethod
    def cast_to_object_from_file_list(cls, vacancies: list):
        list_vacancies = []
        for vacancy in vacancies:
            vacancy_object = cls(vacancy.get("name"),
                                 vacancy.get("alternate_url"),
                                 vacancy.get("salary_from"),
                                 vacancy.get("salary_to"),
                                 vacancy.get("city"),
                                 vacancy.get("experience")
                                 )
            list_vacancies.append(vacancy_object)

        cls.vacancies = list_vacancies

    def to_dict(self):
        return {"name": self.name,
                "alternate_url": self.url,
                "salary_from": self.salary_from,
                "salary_to": self.salary_to,
                "city": self.city,
                "experience": self.experience
                }

    @classmethod
    def add_vacancy(cls, new_vacancy):
        return cls.vacancies.append(new_vacancy)

    @classmethod
    def delete_vacancy(cls, del_vacancy):
        return cls.vacancies.remove(del_vacancy)

    @classmethod
    def sorted_desc_list(cls):
        """ сортируем список """
        # sort_key = lambda vac: vac
        cls.vacancies.sort(reverse=True)

    @classmethod
    def top_n_list(cls, top_n):
        """ выбираем топ вакансий из списка """
        cls.vacancies = cls.vacancies[:top_n]
