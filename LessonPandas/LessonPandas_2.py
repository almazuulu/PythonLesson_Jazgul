import  pandas as pd
# Индексы и установка индекса

# set_index(), reset_index()

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Paris", "London", "Berlin"]
})

df = df.set_index("Name")
print(df)

df2 = pd.DataFrame({
    "Department": ["HR", "IT", "IT", "HR", "Finance", "HR"],
    "Salary": [3000, 4000, 4500, 3200, 5000, 4000]
})

grouped_salary_by_dep_mean = df2.groupby("Department")["Salary"].mean()
print(grouped_salary_by_dep_mean)

grouped_salary_by_dep_max = df2.groupby("Department")["Salary"].max()
print(grouped_salary_by_dep_max)

grouped_salary_by_dep_min = df2.groupby("Department")["Salary"].min()
print(grouped_salary_by_dep_min)

# pivot table
df3 = pd.DataFrame({
    "Department": ["HR", "IT", "IT", "HR", "Finance", "HR", "Finance", "IT"],
    "Gender":       ['F', 'F', 'M', 'M', 'M', 'F', 'F', 'M'],
    "Salary": [3000, 4000, 4500, 3200, 5000, 4000, 3800, 3500]
})

pivot_table = df3.pivot_table(values='Salary',
                              index='Department',
                              columns='Gender',
                              aggfunc='mean') # min, max

print(pivot_table)

df4 = pd.DataFrame({
    "Name": ["Adul", "Adam", "Peter"],
    "Age": [25, None, 31]
})

# проверка на пропуски - помощь при обработке данных с заполнением None значений
print(df4.isnull)

df4 = df4.fillna(0)
print(df4)

# Преобразование данных
df5 = pd.DataFrame({
    "Name": ["Adyl", "Adam", "Peter"],
    "Score": [1350, 1000, 1500]
})

df5["Grade"] = df5["Score"].apply(
    lambda x: "A" if x >= 1450 else "B" if x >= 1300 else "C"
)

print(df5)

# df1, df2 = merge()

df6 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Sapar", "Tilek", "Adam"],
})

df7 = pd.DataFrame({
    "id": [1, 3],
    "salary": ["50000", "40000"],
})


merged_salary_name = pd.merge(df6, df7, on="id")
print(merged_salary_name)

# Создание новых признаков
from datetime import datetime

df8 = pd.DataFrame({
    "Name": ["Adam", "Peter"],
    "Birth year": [1992, 1994]
})

now_year = datetime.now().year

df8["Age"] = now_year - df8["Birth year"]
print(df8)

