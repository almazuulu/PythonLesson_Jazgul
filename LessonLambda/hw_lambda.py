""" 
Task 1

Создайте четыре лямбда-функции: add, subtract, multiply, divide
Создайте словарь operations, где ключи '+', '-', '*', '/' будут 
соответствовать этим функциям

Напишите функцию calculate(a, b, operation), которая использует словарь operations

Пример вызова: calculate(10, 5, '+') должно вернуть 15
"""

# Task 1 - Ответ
def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2

# print(calculator(12, 13, '+'))
# print(calculator(12,3, '/'))

operation = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

# print(operation['add'](100, 5))
# print(operation['divide'](10, 2))
# print(operation ['subtract'] (45,40))

# def math_operation(oper_dict, oper, num1, num2):
#     return(oper_dict[oper](num1, num2))

# print('==========')
# num1 = int(input('Num1: '))
# operation_sign = input('')
# num2 = int(input('Num2: '))


# print(math_operation(operation, operation_sign, num1, num2))
    
    
############## 

""" 
Task 2 - Форматирование данных

# Дан список имен в формате "фамилия, имя"
names = ["Smith, John", "Johnson, Mary", "Williams, Peter"]
# Используя lambda и map, преобразуйте список в формат "Имя Фамилия"
# Результат должен быть: ["John Smith", "Mary Johnson", "Peter Williams"]
"""

# Task 2 - Ответ
# Ваш код тут ...

names = ["Smith, John", "Johnson, Mary", "Williams, Peter"]

#names2 = int(map( lambda name: names[::-1]))
#print(names2)

#def names1(name):
#    return name.split(", ")[1] + " " + name.split(", ")[0]

lambda_split_names = lambda name: name.split(", ")[1] + " " + name.split(", ")[0]

names2 = list(map(lambda_split_names, names))
print(names2)

################
# Task 3 - Фильтрация продуктов

# Task 3 - Ответ

products = [
    {"name": "Laptop", "price": 1000, "rating": 4.5},
    {"name": "Phone", "price": 500, "rating": 4.8},
    {"name": "Tablet", "price": 300, "rating": 4.2},
    {"name": "Watch", "price": 250, "rating": 4.9}
]

"""
# Создайте три разные lambda-функции для фильтрации:
# 1. Продукты дешевле 400
# 2. Продукты с рейтингом выше 4.5
# 3. Продукты дороже 400 и с рейтингом -выше 4.0
"""

def product_less_400(product):
    return product['price'] < 400

rating1 = list(filter(lambda product: product['price'] < 400, products))
# rating2 = list(filter(product_less_400, products))
print('Продукты дешевле 400:', rating1)
# print('Продукты дешевле 400:', rating2)

rating2 = list(filter(lambda product:  product['rating'] > 4.5, products))
print('Продукты с рейтингом выше 4.5:', rating2)


rating3 = list(filter(lambda product: product['price'] > 400 and product['rating'] > 4.0, products))
print('Продукты с рейтингом выше 4.0 и дороже 400:',rating3)


#########################

# Task 4 - Обработка текста

# Дан список предложений
sentences = [
    "Python is AWESOME",
    "LAMBDA functions are COOL",
    "PROGRAMMING is FUN"
]

# Используя lambda и map:
# 1. Преобразуйте все предложения к нижнему регистру
# 2. Посчитайте количество слов в каждом предложении
# 3. Удалите предложения, содержащие слово "fun" (любой регистр)
# 3. Удалите предложения, содержащие отдельное слово "fun" (любой регистр)


# Task 4 - Ответ

transformed = list(map(lambda sentence: sentence.lower(), sentences))
print(transformed)
countWords = list(map(lambda s: len(s.split()), sentences))
print(countWords)

def remove_fun_list_funct(s):
    if "fun" not in s.lower():
        return True
    else:
        return False
    
def remove_fun_list_funct2(s):
    if " fun " not in s.lower():
        return True
    elif " fun" not in s.lower():
        return True
    else:
        return False
    
filtered_without_fun_all = list(filter(
    lambda s: all(word.lower() != 'fun' for word in s.split()), # 1, 2, 3
    sentences
))

remove_fun_list = list(filter(remove_fun_list_funct, sentences))
remove_fun_list2 = list(filter(remove_fun_list_funct2, sentences))
filtered_with_map = list(map(lambda s: s if "fun" not in s.lower() else None, sentences))
print(remove_fun_list)
print(filtered_with_map)
print(remove_fun_list2)
print(filtered_without_fun_all)




