# Магические методы - это специальные методы, которые начинаются и 
# заканчиваются двумя символами подчеркивания (__).
# Они позволяют определять поведение объектов в Python и переопределять стандартные операции.
# Например, если вы хотите, чтобы ваш объект поддерживал операцию сложения, 
# вы можете определить метод __add__.

# __init_ - конструктор
# __str__ - строковое представление объекта
# __repr__ - представление объекта для отладки
# __len__ - длина объекта
# __getitem__ - получение элемента по индексу

# Математические операции
# __add__ - сложение объектов
# __sub__ - вычитание объектов
# __mul__ - умножение объектов
# __truediv__ - деление объектов
# __floordiv__ - целочисленное деление объектов
# __mod__ - остаток от деления объектов
# __pow__ - возведение в степень объектов

# Логическое сравнение
# __lt__ - меньше
# __le__ - меньше или равно
# __eq__ - равно
# __ne__ - не равно
# __gt__ - больше
# __ge__ - больше или равно


# __contains__ - содержит
# __iter__ - итератор
# __call__ - вызов объекта как функции
# __del__ - деструктор


# add - сложение

class Person:
    def __init__(self, name, age, salary=0, children: list[str] = None):
        self.name = name
        self.age = age
        self.salary = salary
        self.children = children
        
    # def display(self):
    #     print(f"Name: {self.name}, Age: {self.age}")
        
    def __add__(self, other):
        if isinstance(other, Person):
            result_age = self.age + other.age
        elif isinstance(other, int):
            result_age = self.age + other
        elif isinstance(other, str):
            result_age = self.age + int(other)
        return result_age
    
    def __sub__(self, other):
        if isinstance(other, Person):
            return self.salary - other.salary
        elif isinstance(other, int):
            return self.salary - other
        elif isinstance(other, str):
            return self.salary - int(other)
        
    def __mul__(self, other):
        if isinstance(other, Person):
            return self.salary * other.salary
        elif isinstance(other, int):
            return self.salary * other
        elif isinstance(other, str):
            return self.salary * int(other)
        
    def __str__(self):
        return f"Name: {self.name}"
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}), salary={self.salary})"
    
    def __truediv__(self, other):
        if isinstance(other, Person):
            return self.salary / other.salary
        elif isinstance(other, int):
            return self.salary / other
        elif isinstance(other, str):
            return self.salary / int(other)
        
    def __mod__(self, other):
        if isinstance(other, Person):
            return self.salary % other.salary
        elif isinstance(other, int):
            return self.salary % other
        elif isinstance(other, str):
            return self.salary % int(other)
        
    def __gt__(self, other):
        if isinstance(other, Person):
            return self.salary > other.salary
        elif isinstance(other, int):
            return self.salary > other
        elif isinstance(other, str):
            return self.salary > int(other)
        
    def __lt__(self, other):
        if isinstance(other, Person):
            return self.salary < other.salary
        elif isinstance(other, int):
            return self.salary < other
        elif isinstance(other, str):
            return self.salary < int(other)
        
    def __floordiv__(self, other):
        if isinstance(other, Person):
            return self.salary // other.salary
        elif isinstance(other, int):
            return self.salary // other
        elif isinstance(other, str):
            return self.salary // int(other)
        
    def __contains__(self, item):
        if isinstance(item, str):
            return item in self.name
        elif isinstance(item, Person):
            return item.name in self.name
        return False
    
    # def __icontains__(self, item):
    #     if isinstance(item, str):
    #         return self.name in item
    #     # elif isinstance(item, Person):
    #     #     return item.name in self.name
    #     return False
    
    def __len__(self):
        return len(self.children) if self.children else 0
    
    def __call__(self, *args, **kwds):
        print(self.name.upper())
        
    
    def __del__(self):
        print(f"Deleting {self.name}...")
        # Здесь можно добавить код для освобождения ресурсов или выполнения других действий при удалении объекта
    
    
        
p1 = Person("Alice", 30, 50000, ["Bob", "Charlie"])
p2 = Person("Bob", 25, 30000, ["Alice", "Peter", "John", "Mary"])

print(p1 + p2)  # Вывод: Name: Alice, Age: 30, Name: Bob, Age: 25
print(p1 + 10) # Вывод: 40
print(p2 + "20") # Вывод: 45


print(p1 - p2)  # Вывод: 20000
print(p1 - 10000) # Вывод: 40000
print(p2 - "5000") # Вывод: 25000

print(p1 * p2)  # Вывод: 1500000000
print(p1 * 2) # Вывод: 100000
print(p2 * "3") # Вывод: 90000

# p1.display()  # Вывод: Name: Alice, Age: 30
print(p1)   # Вывод: Name: Alice
print(p2)   # Вывод: Name: Bob

print(p1 / p2)  # Вывод: 1.6666666666666667
print(p1 / 2) # Вывод: 25000.0
print(p2 / "3") # Вывод: 10000.0

# остаток от деления
print(10 % 3) # Вывод: 1

print(p1 % 15)  # Вывод: 5

# пример __repr__
print(repr(p1))  # Вывод: Person(name=Alice, age=30)
print(repr(p2))  # Вывод: Person(name=Bob, age=25)

print(p1 > p2)  # Вывод: True
print(p1 > 100000) # Вывод: False
print(p2 > "20000") # Вывод: True

print(p1 < p2)  # Вывод: False
print(p1 < 100000) # Вывод: True
print(p2 < "20000") # Вывод: False

print(10//3) # Вывод: 3
print(10/3) # Вывод: 3.3333333333333335

print(p1 // p2)  # Вывод: 1
print(p1 // 2) # Вывод: 25000


# contains - проверка на вхождение
# print(p1 in "Wonderland") # Вывод: False
# print(p1 in "Alice in Wonderland") # Вывод: True

print("Wonderland" in p1) # Вывод: False
print("Alice" in p1) # Вывод: True

# как узнать количествро элементов в списке?
print(len(p1)) # Вывод: 2
print(len(p2)) # Вывод: 4


# вызов объекта как функции
p1() # Вывод: ALICE
p2() # Вывод: BOB

# del - удаление объекта
del p1
del p2

print(p1) # Вывод: NameError: name 'p1' is not defined
print(p2) # Вывод: NameError: name 'p2' is not defined



