""" 
Упражнение: Создание классов и объектов

Создай класс Book, который будет представлять книгу в библиотеке.
Требования:

    У класса должны быть поля (атрибуты):
        
        - title (название книги)

        - author (автор книги)

        - year (год издания)

    Реализуй конструктор __init__(), который принимает название, автора и год.

    Добавь метод display_info(), который выводит информацию о книге в формате:

    "Название: <title>, Автор: <author>, Год: <year>"

1) Создай несколько объектов Book и вызови для них метод display_info().
book1 = Book("1984", "Джордж Оруэлл", 1949)
book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)

book1.display_info()
book2.display_info()

2) Создайте второй метод который отображает title книги в ВВЕРХНЕМ Регистре
def title_upper_letter()
book1.title_upper_letter() -> ДЖОРДЖ ОРУЭЛЛ
book2.title_upper_letter() -> МАСТЕР И МАРГАРИТА
"""

# Ваш код

class Book:
    pass
