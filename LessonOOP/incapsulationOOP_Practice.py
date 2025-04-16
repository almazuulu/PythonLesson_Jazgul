""" 
- Сделать переменные нижеперечисленных классов приватными
- Добавить ко всем геттеры и сеттеры
- Методы оставить публичным
- Вызвать эти объекты и показать чз принт всех их переменные
"""

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        

class Student:
    def __init__(self, student_id, research_work):
        self.student_id = student_id
        self.research_work = research_work
        
    def present_research(self):
        print(f"My student id is {self.student_id} and I have done this kind of research: {self.research_work}")