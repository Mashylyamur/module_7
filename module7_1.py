import requests
from bs4 import BeautifulSoup
page = requests.get(' http://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
curses = soup.find('table', {'class': 'mfd-table mfd-currency-table'}).find_all('tr')

for curs in curses:
    print(f'{curs.get_text(strip=True, separator=" ")}')

