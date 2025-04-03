""" 
Абстракция - второй принцип ООП

Абстракция — это принцип объектно-ориентированного программирования (ООП), 
с помощью которого мы скрываем сложность и показываем только важные детали.
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def display(self):
        pass
    


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def display(self):
        area_calculated = self.area()
        print(f"Круг с радиусом {self.radius} имеет площадь: {area_calculated:.2f}")
    
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    
    def area(self):
        return self.width * self.height
    
    def display(self):
        area_calculated = self.area()
        print(f"Прямоугольник с высотой {self.height} и с шириной {self.width} имеет площадь: {area_calculated:.2f}")


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def display(self):
        area_calculated = self.area()
        print(f"Треугольник с высотой {self.height} и с основанием {self.base} имеет площадь: {area_calculated:.2f}")


circle = Circle(5)
circle.display()
print("="*15)
rectangle = Rectangle(4, 6)
rectangle.display()
print("="*15)
triangle = Triangle(3, 7)
triangle.display()

        
