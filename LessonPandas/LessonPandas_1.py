import pandas as pd

# Работа с сериями
s = pd.Series([20, 10, 30])
print(s)

# Работа с DataFrame
data = {
    'name': ['John', 'Anna', 'Peter', 'Linda', 'Tom'],
    'age': [28, 24, 35, 32, 29],
    'city': ['New York', 'Paris', 'Berlin', 'Moscow', 'London'],
}

print(data)

df  = pd.DataFrame(data)
print(df)

print(df['name'])

print(df[['name', 'age']])

print(df.info()) # информация о DataFrame
print(df.describe()) # статистика по числовым данным
print(df.shape) # размерность DataFrame

df['address'] =['123 Main St', '456 Elm St', '789 Oak St', '45 Baker str', '34 Nap str'] # добавление нового столбца
print(df)

df['age'] = df['age'] + 1 # изменение существующего столбца
print(df)

print(df[df['age'] < 30]) # фильтрация по условию

df_customers = pd.read_csv('customers-1000.csv') # чтение данных из CSV файла

# head - вывод первых 5 строк
print(df_customers.head()) # вывод первых 5 строк

# head(10) - вывод первых 10 строк
print(df_customers.head(10)) # вывод первых 10 строк

# tail - вывод последних 5 строк
print(df_customers.tail()) # вывод последних 5 строк
print(df_customers.tail(100)) # вывод последних 10 строк

for index, row in df_customers.iterrows():
    print(f"Index: {index}, Name: {row['First Name']} {row['Last Name']}, country - {row['Country']}")

# сортировка по странам в df_customers
df_sorted = df_customers.sort_values(by='Country')
print(df_sorted[['First Name', 'Country']].head(100)) # вывод первых 10 строк отсортированного DataFrame

# Те люди которые живут в Бенин

# фильтрация по условию c показом только имен и страны
print(df_customers[df_customers['Country'] == 'Benin'][['First Name', 'Country']]) # фильтрация по условию
print(df_customers[df_customers['Country'] == 'Benin']) 
print(df_customers[df_customers['Country'].isin(['Benin', 'Brazil'])][['First Name', 'Country']]) # фильтрация по условию
# фильтрация по нескольким условиям

df_sorted = df_customers.sort_values(by='Country', ascending=False)
print(df_sorted[['First Name', 'Country']].head(1000)) # вывод первых 10 строк отсортированного DataFrame

# Считаывание по определенным номерам строк
print(df_customers.iloc[1:11]) # вывод строк с 0 по 9

# Считаывание по определенным номерам строк с определенным колонками
print(df_customers.iloc[1:11, [2, 4]]) # вывод строк с 0 по 9 и колонок 0 и 2

# Считывание по loc
print(df_customers.loc[1:11, ['First Name', 'Country']]) # вывод строк с 0 по 9 и колонок 0 и 2

