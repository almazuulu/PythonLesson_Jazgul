# try - except

result = 0
try:
    num1 = int(input("Input num1: "))
    num2 = int(input("Input num2: "))
    result = num1 / num2
except ZeroDivisionError as ze:
    print('Вы не можете делить на ноль!')
except ValueError as ve:
    print('Вы можете делить только на число!')
finally:
    print(result)    
    

listNames = ["Askar", "Aiperi", "Jazgul", "Peter"]

try:
    idx = int(input("Введите число: "))
    print(listNames[idx])
except IndexError:
    print("Ошибка индекса! Такого имени нету!")




def sayHello(n):
    return f"Hello {n}!"

print("....Remaining Code Line 1...")
print(sayHello("Alex"))

print("....Remaining Code Line 2...")