""" 
Домашняя работа


Симуляция умного дома
Создайте абстрактный класс SmartDevice с методами:

turn_on()
turn_off()
get_status()
connect_to_network(network)

Реализуйте устройства:

SmartLight (с уровнем яркости и цветом)
SmartThermostat (с установкой и отслеживанием температуры)
    - self.target_temp, self.curr_temp
    - set_target_temp(target_temp), update_curr_temp(new_temp)
SmartSocket (с мониторингом энергопотребления)
    - self.power_consumption
    - set_power_consumption(new_watt)

Создайте класс SmartHome, который может управлять всеми устройствами 
через абстрактный интерфейс и создавать сценарии автоматизации (например, "Выключить все устройства").
"""

from abc import ABC, abstractmethod

class SmartDevice(ABC):
    
    def __init__(self, name: str):
        self.name = name
        self.is_on = False
        self.network = None
        
    @abstractmethod
    def turn_on(self) -> None:
        pass
    
    
    @abstractmethod
    def turn_off(self) -> None:
        pass
    
    
    @abstractmethod
    def get_status(self) -> None:
        pass
    

    @abstractmethod
    def connect_to_network(self) -> None:
        pass
    
    def display(self):
        print(f"{self.name} ({'включен' if self.is_on else 'выключен'})")
        
# контроль уровня яркости и цвета
class SmartLight(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.brighness = 0 # по умолч от 0 - 100
        self.color = "white"
        
    def turn_on(self) -> None:
        self.is_on = True
        self.brighness = 100
        print(f"{self.name} включен, яркость {self.brighness}%")
    

    def turn_off(self) -> None:
        self.is_on = False
        self.brighness = 0
        print(f"{self.name} выключен")
    
    def get_status(self) -> None:
        return {
            "name": self.name,
            "type": "SmartLight",
            "is_on": self.is_on,
            "brightness": self.brighness,
            "color": self.color,
            "network": self.network
        }
    

    def connect_to_network(self, network) -> None:
        self.network = network
        print(f"{self.name} подключен к сети {self.network}")
        
    
    def set_brighness(self, new_brighness):
        
        if 0 <= new_brighness <= 100:
            self.brighness = new_brighness
            
            if new_brighness > 0 and not self.is_on:
                self.is_on = True
            elif new_brighness == 0 and self.is_on:
                self.is_on = False
            print(f"{self.name} Яркость установлен на {new_brighness}")
        else:    
            print(f"Ошибка уровень яркости должен быть от 0 до 100")
            
    
    def set_color(self, new_color):
        self.color = new_color
        print(f'{self.name} цвет изменен на {new_color}')
            
        