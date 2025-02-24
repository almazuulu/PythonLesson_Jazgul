# Реализация функции не нужна только нужно показать как документировать и аннотировать
# Если хотите и будет время можете реализовать функцию :)
# Пример
def math_fun(num1: int, num2: int)-> int:
    """ 
    Описываете документации в стиле Google....
    """


# Task 1
"""
Создайте функцию calculate_discount, которая принимает изначальную цену 
и процент скидки, и возвращает цену со скидкой. 
Добавьте полную документацию в стиле Google и аннотации типов. 
Функция должна вызывать исключение, если скидка меньше 0 или больше 100.

Пример использования:
calculate_discount(1000, 20) # Вернёт 800.0
calculate_discount(500, 10)  # Вернёт 450.0
"""

# Your code here...


# Task 2
"""
Напишите класс Student с атрибутами для имени, возраста и списка оценок. 
Добавьте метод для вычисления среднего балла. 
Используйте аннотации типов для всех атрибутов и методов, 
а также добавьте документацию в формате NumPy.

Пример использования:
student = Student("Alice", 20, [5, 4, 5, 5])
print(student.calculate_average())  # Вернёт 4.75
"""

# Your code here...


# Task 3
"""
Создайте функцию filter_users, которая принимает список словарей 
с данными пользователей и минимальный возраст. 
Функция должна возвращать отфильтрованный список пользователей 
старше указанного возраста.

Пример входных данных:
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 19},
    {"name": "Charlie", "age": 30}
]
filter_users(users, 20)  # Вернёт список с Alice и Charlie
"""

# Your code here...


# Task 4
"""
Разработайте функцию process_data, которая принимает кортеж чисел 
произвольной длины и возвращает словарь со следующей статистикой: 
минимальное значение, максимальное значение, среднее значение.

Пример использования:
process_data((1, 2, 3, 4, 5))
# Вернёт {"min": 1, "max": 5, "average": 3.0}
"""

def process_data(nums: tuple[int, ...]) -> dict[str, float]:
    """ 
    Function that accepts tuple of integer numbers and then gives 
    stats including min, max and average values out of the nums
    
    Params:
        nums(tuple[int, ...]): Tuple of integer numbers as input
    Return:
        stats(dict[str, float]): Stats of min, max average values that's been found from the calculation
    Exception:
        ValueError, ZeroDevisionError
    """
    pass


# Task 5
"""
Создайте функцию merge_sets, которая принимает произвольное 
количество множеств строк и возвращает:
1. Объединение всех множеств
2. Пересечение всех множеств
3. Уникальные элементы, которые встречаются только в одном множестве

Пример использования:
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set3 = {"c", "d", "e"}
merge_sets(set1, set2, set3)
# Вернёт:
# {
#   "union": {"a", "b", "c", "d", "e"},
#   "intersection": {"c"},
#   "unique": {"a", "e"}
# }
"""

def merge_sets(s1: set[str], s2: set[str], s3: set[str]) -> dict[str, set[str]]:
    """ 
    Function that can show functionalities of set by finding intersection, unique, union values
    
    Params:
        s1 (set[str]): First set of str values
        s2 (set[str]): Second set of str values
        s3 (set[str]): Third set of str values
    Return:
        Stats (dict[str, set[str]]): Stats of uninon, intersection, unique values
    """
    pass
