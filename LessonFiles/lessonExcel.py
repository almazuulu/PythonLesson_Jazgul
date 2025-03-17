# python3 -m venv venv - создание виртуального окружения (Windows/ Mac OS)
# source .venv/bin/activate - активация виртуального окружения для Mac OS
# .\venv\Scripts\activate - активация виртуального окружения для Windows

# pip install pandas - установка пакета pandas - инструмент анализа csv, excel
# pip install openpyxl - установка пакета openpyxl - помощник чтения/записи Excel

import pandas as pd

# Чтение всего excel файла
df = pd.read_excel('LessonFiles/food.xlsx', usecols=['City', 'Category', 'Product', 'Qty', 'TotalPrice'])
# print(df.head(30))
# print(df[['ID']['City']])
# print(df.tail(20))
# print(df[df['Category'] == 'Cookies'].head(30))
# print(df[df['City'].isin(["San Diego", "New York"])].head(50))

# print(df.iloc[95:100, 1:4])
print(df.info())
print(df.describe())
