# Example 2

words = ['apple', 'Banana', 'Appricot', 'Cherry', 'Avocado']
# ['Apple', 'Appricot', 'Avocado'] # a -> apple -> Apple

def isWordA(w):
    if w.capitalize().startswith('A'): # if w[0].capitalize() == 'A'
        return True
    else:
        return False
    

starts_with_a = lambda w: True if w.capitalize().startswith('A') else False

filteredList = list(filter(isWordA, words))
filteredList_lambda = list(filter(starts_with_a, words))

print(filteredList)
print(filteredList_lambda)

#####################
wordsProgramming = ['python', 'java', 'javascript', 'c++', 'go']
# ['go', 'c++', 'java', 'python', 'javascript']

# 1 - sort
# 2 - len() - сделать функцию которая выявляет длину - len(w)
# 3 lambda n: len(w)
# list(sorted, key = lambda n: len(w))

def findLenWords(w):
    return len(w)

lenWordsLambda = lambda w: len(w)

sortedWords = sorted(wordsProgramming, key=lenWordsLambda)
sortedWords_len = sorted(wordsProgramming, key=len)

print(sortedWords)
print(sortedWords_len)