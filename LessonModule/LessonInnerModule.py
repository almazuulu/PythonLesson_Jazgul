# Встроенные модули - math, random, datetime

import math

# математические значения
print(math.pi)
print(math.e)
print(math.inf)

# Округление и преобразование
print(f"Округление вниз: {math.floor(4.7)}") # 4
print(f"Округление вверх: {math.ceil(4.3)}") # 5
print(f"Округление к ближ целому {math.trunc(5.9)}")

# Степень, корни и логарифмы
print(f'2 в степени 10: {math.pow(2, 10)}')
print(f'Square Root of 16: {math.sqrt(16)}')
print(f'Triple Root of 27: {math.cbrt(27)}')
print(f'Log math: {math.log(10)}') # 2.3025
print(f'Triple Root of 27: {math.log2(8)}')  # 3
print(f'Log 100 with basic of 10: {math.log10(100)}') #2


# factorial nums - 5! = 5 * 4 * 3 * 2 * 1
print(f'Factorial num of 5 is {math.factorial(5)}')

# Collections - counter, defaultdict, namedtuple, most_common

# import collections # collections.Counter()
# from collections import Counter - Counter()
from collections import Counter, defaultdict, namedtuple

listFruits = ["Apple", "Banana", "Apple", "Appricot", "Ananas", "Apple", "Banana", "Coconut", "Cucumber", "Cucumber"]
count_fruit = Counter(listFruits)
print(count_fruit)

print(f'Top 3 fruits: {count_fruit.most_common(3)}')

chars = "asdasfdjosdijforihiefunwcuneirghoesnfknacirehuthosdfsdkbfjshaorfwerwfcdscerglerwjgejwepqjgsdafdaspfd"
chars_count = Counter(chars)
print(chars_count)



# Defaultdict
contacts = {
    "Father": "+996555111222",
    "Mother": "+996555333444",
    "Brother": "+996777888999"
}

# print(contacts["Sister"])

fruits_by_color = defaultdict(list)
fruits_by_color['red'].append('apple')
fruits_by_color['red'].append('straweberry')
fruits_by_color['yellow'].append('banana')
fruits_by_color['yellow'].append('lemon')
fruits_by_color['green'].append('water melon')

print(f"Fruits by color: {dict(fruits_by_color)}")
print(fruits_by_color["pink"])
print(f"Fruits by color: {dict(fruits_by_color)}")

# NamedTuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
p2 = Point(19, 32)
print(f'Point: {p}')
print(f'Point2: {p2}')

# Student records
Student = namedtuple('Student', 'name age group grades')
student1 = Student('Petr Ivanov', 22, '101', [3, 4, 5, 5])
print(f"Student: {student1}")
print(f'Studen age: {student1.age}')

# Datetime
# import datetime # datetime, date, time, timedelta, timezone
from datetime import datetime, date
# Current time and date

now = datetime.now()
print(now)

today = date.today()
print(today)
print(today.month)
print(today.day)
print(today.year)

print(f'today is: {today.day}/{today.month}/{today.year}')


# Sys - argv
import sys
print(sys.argv)
print(sys.version)
print(sys.executable)


# OS - working with OS
import os

current_dir = os.getcwd()
print(current_dir)

os.makedirs("new_folder", exist_ok=True)
os.makedirs("new_folder2", exist_ok=True)
os.makedirs("new_folder3/sub_folder1", exist_ok=True)

files = os.listdir("LessonLambda")
print(files)


# random - предназначена для работы с рандомными числами
import random

random_float = random.random()
print(random_float)

# random range numb
random_float_random = random.uniform(10.5, 20.5)
print(random_float_random)

# Random int numbers
random_int_numb = random.randint(1, 200)
print(random_int_numb)

# random value with step
random_step = random.randrange(0, 101, 5)
print(random_step)


# Choice, shuffle, sample
names = ["Bektur", "Aiperi", "Kanat", "Adilet", "Muhammad", "Daud", "Aselya"]
print(random.choice(names))
random.shuffle(names)
print(names)

mayHolidayList = random.sample(names, k=3)
print(mayHolidayList)
