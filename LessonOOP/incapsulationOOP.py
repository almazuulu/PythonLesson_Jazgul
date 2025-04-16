""" 
Инкапсуляция — это принцип ООП (объектно-ориентированного программирования), который означает скрытие внутреннего устройства объекта.
Другими словами: объект сам решает, что можно показывать, а что — нет.

Это помогает:
    - защитить данные от случайных изменений,
    - контролировать доступ к ним,
    - упростить использование объекта (не нужно знать, как он устроен внутри).
    
    
Вид доступа | Синтаксис | Описание

Публичный | name | Можно свободно использовать
Защищённый | _name | По соглашению: "не трогай, если не знаешь, что делаешь"
Приватный | __name | Python "прячет" это имя (name mangling)
"""

class BankAccount:
    def __init__(self, owner, balance, address):
        self.owner = owner
        self.__balance = balance
        self.__address = address
    
    # дали разрешение на просмотр - модификатор доступа getter
    def get_balance(self):
        return self.__balance
    
    # дается разрешение на изменение - модификатор доступа setter
    def set_address(self, new_address):
        self.__address = new_address

    def get_address(self):
        return self.__address
    
    def __make_upper(self, value_change):
        return value_change.upper()

    
    def display(self):
        print("*******************************")
        print(self.__make_upper(self.owner))
        print(self.__make_upper(str(self.__balance)))
        print(self.__make_upper(self.__address))
        print("*******************************")
        

bac1 = BankAccount("Oleg Tinkof", 50000, "Lev Tolstoy 777")

print(bac1.owner)
print(bac1.get_balance())
bac1.set_address("Panfilova 123")
print(bac1.get_address())
bac1.display()
# bac1.__make_lower("Some")