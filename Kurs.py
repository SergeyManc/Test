import requests  # Модуль для обработки URL
from bs4 import BeautifulSoup   # Модуль для работы с HTML

URL = 'https://www.cbr.ru/currency_base/daily/'
HEADERS = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'

#Не разобрался как парсить сайт ЦБ
# def get_html(url, params=None):
#     r = requests.get(url, params=params)
#     return r
#
# def get_content(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('table', class_ = 'data')
#     name = []
#     for item in items:
#         name.append({
#             'title' : item.find('tbody', class_ = '' ).get_text()
#         })
#         print(name)
#         print(len(name))
#     print(items)
#
#
# def parse():
#     html = get_html(URL)
#
#     if (html.status_code) == 200:
#        get_content(html.text)
#     else:
#         print("Error")
#
#
#
# parse()