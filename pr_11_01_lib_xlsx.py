import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_xlsx = pd.read_excel('RC_F01_11_2010_T13_11_2024_EURO.xlsx')

data_xlsx['data'] = pd.to_datetime(data_xlsx['data'])   # даты в формате datetime

print(data_xlsx.head())

#
plt.plot(data_xlsx['data'], data_xlsx['curs Euro'], label='Курс Евро', color='blue')
plt.plot(data_xlsx['data'], data_xlsx['curs USD'], label='Курс USD', color='red')

# вычисление линии тренда для Евро
z_euro = np.polyfit(range(len(data_xlsx['curs Euro'])), data_xlsx['curs Euro'], 1)
p_euro = np.polyval(z_euro, range(len(data_xlsx['curs Euro'])))
plt.plot(data_xlsx['data'], p_euro, label='Тренд Евро', color='blue', linestyle='--')
print(z_euro[0], z_euro[1])

# вычисление линии тренда для USD
z_usd = np.polyfit(range(len(data_xlsx['curs USD'])), data_xlsx['curs USD'], 1)
p_usd = np.polyval(z_usd, range(len(data_xlsx['curs USD'])))
plt.plot(data_xlsx['data'], p_usd, label='Тренд USD', color='orange', linestyle='--')
print(z_usd[0], z_usd[1])

# добавление заголовка и подписи осей
plt.title('Динамика курса валюты Евро c 01.11.2010 по 13.11.2024 ')
plt.xlabel('Даты')
plt.ylabel('Курс')
plt.legend()

plt.show()
