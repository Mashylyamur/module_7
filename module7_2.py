import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

page = requests.get(' http://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
curses = soup.find('table', {'class': 'mfd-table mfd-currency-table'}).find_all('tr')
data = [curs.get_text(strip=True, separator=" ") for curs in curses]
x = [str(data[2:11])]
s = data[13:19]
y = [float(i) for i in s]

plt.plot(x, y)
plt.grid()
plt.show()

