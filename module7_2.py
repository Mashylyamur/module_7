import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

page = requests.get(' http://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
curses = soup.find('table', {'class': 'mfd-table mfd-currency-table'}).find_all('tr')
data = [curs.get_text(strip=True, separator=",") for curs in curses]

xs = []
ys = []

plt.plot(xs, ys)
plt.grid()
plt.show()

