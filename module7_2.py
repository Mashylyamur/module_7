import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

page = requests.get(' http://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
curses = soup.find('table', {'class': 'mfd-table mfd-currency-table'}).find_all('tr')
data = [curs.get_text(strip=True, separator=" ") for curs in curses]

e = []
for i in data:
    e += str(i).split()
x = []
y = []
for i in range(len(e) - 1, 3, -4):
    x.append(str(e[i - 2]))
    y.append(float(str(e[i - 1])))
plt.plot(x, y)
plt.grid()
plt.show()

