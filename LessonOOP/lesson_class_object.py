# Без ООП - процедурный подход

car1_brand = "Toyota"
car1_model = "Camry"
car1_year = 2021

car2_brand = "BMW"
car2_model = "X5"
car2_year = 2018

tel_brand = "iPhone"
tel_model = "16 Pro Max"
tel_year = 2024

def display_car(brand, model, year):
    print(f"{brand} {model}, {year} года")

# display_car(car1_brand, car1_model, car1_year)
# display_car(car2_brand, car2_model, car2_year)
# display_car(tel_brand, tel_model, tel_year)

########### OOP подход #################
# Создание классов и объектов

class Car:
    def __init__(self, brand, model, year):
        self.brandLocal = brand
        self.modelLocal = model
        self.yearLocal = year
        
    def display_info(self):
        print(f"{self.brandLocal} {self.modelLocal}, {self.yearLocal} года")


car1 = Car("BMW", "X5", 2019)
car2 = Car("Toyota", "Camry", 2022)

car1.display_info()
car2.display_info()















