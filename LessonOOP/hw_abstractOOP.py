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
        
# Установка и отслеживание температуры
class SmartThermostat(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.target_temp = 20
        self.curr_temp = 20
        
    
    def turn_on(self) -> None:
        self.is_on = True
        print(f"{self.name} поддерживается температура {self.target_temp}")
    

    def turn_off(self) -> None:
        self.is_on = False
        print(f"{self.name} выключен")
    
    def get_status(self) -> None:
        return {
            "name": self.name,
            "type": "SmartThermostat",
            "is_on": self.is_on,
            "current_temperature": self.curr_temp,
            "target_temperature": self.target_temp,
            "network": self.network
        }
    

    def connect_to_network(self, network) -> None:
        self.network = network
        print(f"{self.name} подключен к сети {self.network}")
        
    
    def set_target_temp(self, target_temp):
        self.target_temp = target_temp
        print(f"{self.name} целевая температура установлена на {target_temp}")
        
    def update_curr_temp(self, update_temp):
        self.curr_temp = update_temp
        print(f"{self.name} новая температура установлена на {update_temp}")
    
    
class SmartSocket(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.power_consumption = 0
        
    
    def turn_on(self) -> None:
        self.is_on = True
        print(f"{self.name} включен)")
    

    def turn_off(self) -> None:
        self.is_on = False
        print(f"{self.name} выключен")
    
    def get_status(self) -> None:
        return {
            "name": self.name,
            "type": "SmartSocket",
            "is_on": self.is_on,
            "power_consumption": self.power_consumption,
            "network": self.network
        }
    

    def connect_to_network(self, network) -> None:
        self.network = network
        print(f"{self.name} подключен к сети {self.network}")
        
    
    def set_power_consumption(self, new_watts):
        if self.is_on:
            self.power_consumption = new_watts
            print(f"{self.name} текущее энергопотребление {new_watts} ВТ")
        else:
            print(f"Ошибка {self.name} выключена, невозможно установить энергоптребление")



class SmartHome:
    "Класс для управления умным домом"
    
    def __init__(self, name):
        self.name = name
        self.devices = dict[str, SmartDevice] = {}
        self.network = f"{name}_network"
        print(f"Умный дом '{name}' создан с сетью {self.network}")
        
    
    def add_device(self, device: SmartDevice):
        # Ваш код реализации
        pass
    
    def remove_device(self, device: SmartDevice):
        # Ваш код реализации
        pass
    
    def get_device_name(device_name):
        # Ваш код реализации
        pass
    
    
    def turn_on_all_devices(self):
        # Ваш код реализации
        pass
    
    
    def turn_off_all_devices(self):
        # Ваш код реализации
        pass
    
    
    def night_mode(self):
        # ночной режим - условие - опр градус, свет, розетка
        pass
    
    def day_mode(self):
        # условие опр градус, свет, розетка
        pass
    
    def energy_saving_mode(self):
         # условие опр градус, свет, розетка
        pass
    
    
    def get_all_devices_status(self):
        pass
    
    

# Пример использования:
if __name__ == "__main__":
    # Создаем умный дом
    home = SmartHome("Мой умный дом")
    
    # Создаем устройства
    light_living = SmartLight("Свет в гостиной")
    light_kitchen = SmartLight("Свет на кухне")
    thermostat = SmartThermostat("Термостат")
    socket_tv = SmartSocket("Розетка ТВ")
    socket_kitchen = SmartSocket("Розетка кухня")
    
    # Добавляем устройства в умный дом
    home.add_device(light_living)
    home.add_device(light_kitchen)
    home.add_device(thermostat)
    home.add_device(socket_tv)
    home.add_device(socket_kitchen)
    
    # Включаем все устройства
    home.turn_on_all_devices()
    
    # Настройка отдельных устройств
    light_living.set_brightness(70)
    light_living.set_color("blue")
    thermostat.set_target_temperature(23)
    thermostat.update_current_temperature(21)
    socket_tv.set_power_consumption(120)
    
    # Выводим статус всех устройств
    print("\nСтатус всех устройств:")
    for name, status in home.get_all_devices_status().items():
        print(f"{name}: {status}")
    
    # Применяем сценарий ночного режима
    print("\nВключаем ночной режим:")
    home.night_mode()
    
    # Выключаем все устройства
    print("\nВыключаем все устройства:")
    home.turn_off_all_devices()
           