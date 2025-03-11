def even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def find_max(numbers):
    if not numbers:
        raise ValueError("Список пуст!")
    return max(numbers)

def averageNum(numbers):
    if not numbers:
        raise ValueError("Список пуст!")
    return sum(numbers) / len(numbers)