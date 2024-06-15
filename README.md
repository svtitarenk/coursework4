
 Курсовая работа 4. ООП (Python)
Программа, которая получает информацию о вакансиях с платформы hh.ru в России, позволяет удобно работать с ней: добавлять, фильтровать, удалять, сохраняет ее в файл.

# Реализация по шагам:
## 1. Запрос вакансий через open API HeadHunter (API и библиотека requests)
##### 1.1. Формирование запроса на получение списка вакансий через открытые методы HH API используя request и параметры запроса (профессия, сумма ожидаемой зарплаты)

Ссылки на файлы:

[hh.py](https://drive.google.com/file/d/1JFM9V2eMNvnbn9JpyrJAOZ6Je3VPR9z6/view?usp=sharing)

[vacancies.json](https://drive.google.com/file/d/1BVRjq02dCHADlg5a7BZXETGe0Pu9e-ob/view?usp=sharing)

Документация для сбора вакансий с hh.ru

[Ссылка на API](https://github.com/hhru/api/)

## 2. Получение json словаря со списком вакансий 
##### 2.1 Получение словаря, 
##### 2.2 Присвоение Экземпляров класса каждой вакансии

## 3. Преобразование в экземпляры класса

## 4. Доп.фильтрация полученного списка
##### 4.1 Дополнительная фильтрация по содержанию ключевых слов в вакансии
##### 4.2 Сортировка списка по убыванию зарплаты через дандер метод сравнения экземпляров класса
##### 4.3. Формирование окончательного списка топ вакансий для сохранения в файл и вывод пользователю


### Файл запроса API HH

**`hh_api.py`**


```import json

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
        # while self.params.get('page') != 2:
        response = requests.get(self.url, headers=self.headers, params=self.params)
        vacancies = response.json()['items']
        self.vacancies.extend(vacancies)
            # self.params['page'] += 1

        return self.vacancies
   ```


#### Пример использования
Данный пример можно использовать как подсказку к началу реализации. Итоговая реализация может иметь любое количество классов, функций и их названий, другой принцип организации.

##### Создание экземпляра класса для работы с API сайтов с вакансиями
```hh_api = HeadHunterAPI()```

##### Получение вакансий с hh.ru в формате JSON
```hh_vacancies = hh_api.get_vacancies("Python")```

##### Преобразование набора данных из JSON в список объектов
```vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)```

##### Пример работы контструктора класса с одной вакансией
```vacancy = Vacancy("Python Developer", "", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")```

##### Сохранение информации о вакансиях в файл
```
json_saver = JSONSaver()
json_saver.add_vacancy(vacancy)
json_saver.delete_vacancy(vacancy)
```



##### Функция для взаимодействия с пользователем
```def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000```
    
    ```filtered_vacancies = filter_vacancies(vacancies_list, filter_words)```

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)
```

```if __name__ == "__main__":
    user_interaction()
   ```

