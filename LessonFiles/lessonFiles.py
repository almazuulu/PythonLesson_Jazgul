import os
""" 
Режимы при операции с файлами

-r - чтение (по умолчанию)
- w - запись 
- a - запись с дополнением
- r+ - чтение и запись
- b - чтение контента с медиафайлов
"""

# Базовая операции при работе с файлом

# чтение с файла

# try:
#     file = open('files/my_file2.txt', 'r')
#     try:
#         content = file.read()
#         print(type(content))
#         print(content)
    
#     except FileNotFoundError as fe:
#         print(f'Файл не найден, детали ошибки: {fe}')

#     finally:
#         file.close()
        
# except Exception as e:
#         print(f'Детали ошибки {e}')
    
from datetime import datetime

def full_content_read(file_name: str):    
    with open(file_name, 'r') as file:
        content = file.read()
        print(type(content))
        print(content)
        
def read_line_by_line(file_name: str):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print(lines)
        for line in lines:
            print(line.strip())
            
def read_line_by_line2(file_name: str):
    with open(file_name, 'r') as file:
        for line in file:
            print(line.strip())
            

def write_to_new_file(file_path: str):
    # Запись файлов с режимом записи w
    with open(file_path, 'w', encoding='utf8') as file:
        file.write("Пример контента который я записываю\n")
        file.write("Это вторая строка файла")
        
def write_user_input(file_name: str):
    name = input('Введите свое имя: ')
    text_input = input("Введите свою жалобу: ")
    now = datetime.now()
    
    with open(f'{file_name}_{now.day}-{now.month}-{now.year}.txt', 'w', encoding="utf8") as file:
        file.write(f"Имя жалующегося: {name}\n")
        file.write(f"Текст жалобы: \n")
        file.write(f"------------------ \n")
        file.write(f"{text_input}\n")
        file.write(f"------------------ \n")

def append_from_resto(file_name:str):
    answer = input("Введите ответ заведения: ")
    now = datetime.now()
    
    with open(f"{file_name}_{now.day}-{now.month}-{now.year}.txt", 'a', encoding="utf8") as file:
        file.write("Ответ от заведения: \n")
        file.write(f"------------------ \n")
        file.write(f"{answer}\n")
        file.write(f"------------------ \n")
 


if __name__ == "__main__":
    file_path = 'files/my_file.txt'
    file_write_new = 'files/new_file.txt'
    file_comply = "files/comply"
    # full_content_read('files/my_file.txt')
    
    # read_line_by_line(file_path)
    # read_line_by_line2(file_path)
    
    # write_to_new_file(file_write_new)
    # write_user_input(file_comply)
    # append_from_resto(file_comply)
        






