""" 
1) Музыкальные инструменты

Создай абстрактный класс Instrument с методом play().

Реализуй классы:

    - Guitar
    - Drum
    - Piano

Каждый инструмент должен по-своему выводить сообщение о том, как он играет.
"""

from abc import ABC, abstractmethod

class MusicalInstrument(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass 
    

class Guitar(MusicalInstrument):
    def __init__(self, sound):
        self.sound = sound
        
    def make_sound(self):
        print(f"Guitar makes sound like: '{self.sound}'")
        

guitar = Guitar("zzzz-zzz-zz")
guitar.make_sound()