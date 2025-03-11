from My_module import addition, subtract, multiply, capitalize_text, count_vowels, reverse_string
from utils.list_utils import even_numbers, find_max, averageNum


def main():

    print(addition(5, 3))
    print(subtract(10, 4))
    print(multiply(2, 6))

    print(capitalize_text("hello world"))
    print(count_vowels("Jazgul"))
    print(reverse_string("python"))


    numbers = [1, 2, 3, 4, 5, 6]
    # print(filter_even_numbers(numbers))
    print(find_max(numbers))
    print(averageNum(numbers))
    print(even_numbers(numbers))
    # print(calculate_average(numbers))


if __name__ == "__main__":
    main()