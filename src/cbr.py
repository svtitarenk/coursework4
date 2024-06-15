import requests
from abc import ABC, abstractmethod
from lxml import etree
from datetime import date, datetime


class Parser:

    @abstractmethod
    def load_data(self, keyword=None):
        pass


class CurrencyCourseAPI(Parser):
    courses = {}

    def __init__(self):
        current_date = datetime.now().date()
        formatted_date = current_date.strftime('%d/%m/%Y')
        self.url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=' + formatted_date

    def load_data(self, keyword=None):
        response = requests.get(self.url)
        names = ('KZT', 'USD', 'EUR')
        if response.status_code == 200:
            text_xml = response.content
            elements = etree.fromstring(text_xml, parser=etree.XMLParser(encoding='cp1251', recover=True))
            for currency in elements:
                for item in currency:
                    if item.text in names:
                        string_value = currency.find('Value').text
                        str_nominal = currency.find('Nominal').text
                        value = float(string_value.replace(',', '.')) / float(str_nominal.replace(',', '.'))
                        value = round(value, 2)
                        self.courses[item.text] = value
            return self.courses


if __name__ == "__main__":
    cbr = CurrencyCourseAPI()
    prnt = cbr.load_data()
    print(prnt)

