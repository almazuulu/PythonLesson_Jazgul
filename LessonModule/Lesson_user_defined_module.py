from new_folder import find_two_sums, find_three_sums, find_sum_four, find_minsu_nums
from new_folder2 import sayHello, sayHello2
from LessonLambda.lambda_practise import starts_with_a

def exampleFunc(some):
    pass

def exampleFunc2(some):
    pass


if __name__ == "__main__":
    print(find_two_sums(2, 3))
    print(find_three_sums(10, 15, 20))
    print(sayHello("Altyn"))
    print(sayHello2("Samat"))
    print(find_minsu_nums(10, 5))

    words = ['apple', 'Banana', 'Appricot', 'Cherry', 'Avocado']
    listWords = list(filter(starts_with_a, words))
    print(listWords)
