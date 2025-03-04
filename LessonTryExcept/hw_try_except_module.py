# Домашнее задание: Модули и обработка исключений

"""
Условие:
1. Создайте папку my_modules и в ней два файла модулей:
   - math_operations.py (с функциями perform_addition, perform_subtraction, perform_multiplication, perform_division)
   - string_operations.py (с функциями capitalize_text, count_vowels, reverse_string)

2. Создайте папку utils и в ней файл list_utils.py с функциями:
   - filter_even_numbers - фильтрует список и возвращает только четные числа
   - find_max - находит максимальное число в списке
   - calculate_average - вычисляет среднее арифметическое списка чисел

3. В основном файле (main.py):
   - Импортируйте все созданные модули
   - Примените каждую функцию из импортированных модулей с примерами
   - Напишите блок try-except для деления чисел, введенных пользователем, обрабатывая возможные исключения
   - Напишите блок try-except для работы со списком, чтобы обработать исключение IndexError
   - Создайте lambda-функцию для фильтрации строк, которые начинаются с определенной буквы

4. Документируйте каждую функцию с помощью docstring
"""

# Вот структура файлов для выполнения:

# Файл: my_modules/math_operations.py

def perform_addition(a, b):
    """
    Выполняет сложение двух чисел.
    
    Args:
        a: Первое число
        b: Второе число
        
    Returns:
        Сумма двух чисел
    """
    # Ваш код:
    pass

def perform_subtraction(a, b):
    """
    Выполняет вычитание второго числа из первого.
    
    Args:
        a: Первое число
        b: Второе число
        
    Returns:
        Разность a - b
    """
    # Ваш код:
    pass

def perform_multiplication(a, b):
    """
    Выполняет умножение двух чисел.
    
    Args:
        a: Первое число
        b: Второе число
        
    Returns:
        Произведение двух чисел
    """
    # Ваш код:
    pass

def perform_division(a, b):
    """
    Выполняет деление первого числа на второе.
    
    Args:
        a: Делимое
        b: Делитель
        
    Returns:
        Результат деления a на b
    """
    # Ваш код:
    pass
"""

# Файл: my_modules/string_operations.py
"""
def capitalize_text(text):
    """
    Преобразует первую букву каждого слова в верхний регистр.
    
    Args:
        text: Входная строка
        
    Returns:
        Строка с заглавными первыми буквами каждого слова
    """
    # Ваш код:
    pass

def count_vowels(text):
    """
    Подсчитывает количество гласных букв в строке.
    
    Args:
        text: Входная строка
        
    Returns:
        Количество гласных букв
    """
    # Ваш код:
    pass

def reverse_string(text):
    """
    Переворачивает строку.
    
    Args:
        text: Входная строка
        
    Returns:
        Перевернутая строка
    """
    # Ваш код:
    pass
"""

# Файл: utils/list_utils.py
"""
def filter_even_numbers(numbers):
    """
    Фильтрует список и возвращает только четные числа.
    
    Args:
        numbers: Список чисел
        
    Returns:
        Список, содержащий только четные числа
    """
    # Ваш код:
    pass

def find_max(numbers):
    """
    Находит максимальное число в списке.
    
    Args:
        numbers: Список чисел
        
    Returns:
        Максимальное число
    """
    # Ваш код:
    pass

def calculate_average(numbers):
    """
    Вычисляет среднее арифметическое списка чисел.
    
    Args:
        numbers: Список чисел
        
    Returns:
        Среднее арифметическое
    """
    # Ваш код:
    pass
"""

# Файл: main.py
"""
# Импортируйте все созданные модули
# Ваш код:


def main():
    # Примените каждую функцию из импортированных модулей с примерами
    # Ваш код:
    
    
    # Блок try-except для деления чисел
    try:
        # Ваш код:
        pass
    except ZeroDivisionError:
        # Ваш код:
        pass
    except ValueError:
        # Ваш код:
        pass
    finally:
        # Ваш код:
        pass
    
    # Блок try-except для работы со списком
    names = ["Алексей", "Мария", "Иван", "Елена"]
    try:
        # Ваш код:
        pass
    except IndexError:
        # Ваш код:
        pass
    
    # Создайте lambda-функцию для фильтрации строк
    # Ваш код:
    
    
if __name__ == "__main__":
    main()


# Дополнительное задание:
"""
1. Добавьте к math_operations.py функцию calculate_power(base, exponent), которая вычисляет base в степени exponent
2. Добавьте к string_operations.py функцию count_words(text), которая подсчитывает количество слов в строке
3. Добавьте к list_utils.py функцию remove_duplicates(items), которая удаляет дубликаты из списка
4. В main.py добавьте обработку еще одного типа исключений на ваш выбор
"""