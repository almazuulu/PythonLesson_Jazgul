def read_debts_into_dict(filename: str):
    # прочитать файл
    # каждое содержимое из файла записать в словарь
    """ 
    Результат списка который должен быть после прочтения из файла
    
    {
        "Улан": 500,
        "Адилет": 200,
        "Айпери": 2000
    }
    """
    
    with open(filename, 'r', encoding='utf8') as file:
        content = file.readlines()
        
        dict_debts = {}
        for line in content:
            name, money = line.split(' - ')
            amount, _ = money.split( )
            dict_debts[name] = int(amount)
    
    return dict_debts
            
            

def write_new_debts(filename: str):
    """ 
    Функция, которая записывает новые долги в сущ. текстовый файл
    
    Есть в files/debts.txt:
    
    Улан - 500 сом
    Адилет - 200 сом
    Айпери - 2000 сом
    
    после добавление должен получиться окончательный вот такой файл:
    
    Улан - 500 сом
    Адилет - 200 сом
    Айпери - 2000 сом
    Кылыч - 1500 сом
    Усон - 1300 сом
    ---------------
    ИТОГ:  5500 сом
    """
    
    num_of_debts = int(input('Укажите кол-во записей для файла: '))
    
    with open(filename, 'a', encoding='utf8') as file:
        dict_debts = read_debts_into_dict(filename)
        previous_total_amt = sum(dict_debts.values()) # [500, 200, 2000]
        current_total_amt = 0
        file.write('\n')
        
        for i in range(num_of_debts):
            name = input(f'Имя {i+1}-го должника: ')
            amount_money = int(input(f'Укажите сумму долга для {i+1}-го должника: '))
            
            current_total_amt += amount_money
            
            file.write(f'{name} - {amount_money} сом\n')
        
        file.write('-----------------\n')
        file.write(f'ИТОГ:   {previous_total_amt + current_total_amt} сом')
        print(f'Файл успешно отредактирован!')
    

if __name__ == "__main__":
    file_name = "debts.txt"
    
    print(read_debts_into_dict(file_name))
    write_new_debts(file_name)
    
    
    
    
    