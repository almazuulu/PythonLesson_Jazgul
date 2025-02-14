# Lambda expression

# Explanations
def sayHello(name):
    print(name)
    
lambdaSayHello = lambda name: print(name)
lambdaSayHello2 = lambda name: name
    
def sayHello2(name):
    return name + ' how are you?'


sayHello('Kanat')
print(sayHello2('Kanat'))

sayHelloInfo = sayHello2('Larisa')
print(sayHelloInfo)

lambdaSayHello('Kolya')
print(lambdaSayHello2('Adyl'))


# mathematic operations

def mathFun(num1, num2, num3):
    findLargest = max([num1, num2, num3])
    return (num1 + num2 + num3) + findLargest

lambdaMaxFun = lambda num1, num2, num3: num1 + num2 + num3

print(mathFun(4, 5, 6))
print(lambdaMaxFun(4, 5, 6))


def mathOper(num1, num2, oper1, oper2):
    result1 = oper1(num1, num2)
    result2 = oper2(num1, num2)
    
    overallResult = result1 + result2
    return overallResult

resultMathOper = mathOper(10, 20, lambda n1, n2: n1 + n2, lambda n1, n2: n1* n2)
resultMathOper2 = mathOper(10, 5, lambda n1, n2: n1 // n2, lambda n1, n2: n1 - n2)

print(resultMathOper)
print(resultMathOper2)

# Default params
lambdaExpDefParam = lambda n1, n2, n3=100: n1 + n2 + n3
print(lambdaExpDefParam(10, 20, 200))

# Map() - Map функция - list, set, tuple, dict
def powerByThree(n):
    return n**3

lambdaPowerByThree = lambda n: n**3

print(powerByThree(2))

myList = [2, 3, 4, 5]

makeList = []
for i in myList:
    numThreePower = powerByThree(i)
    makeList.append(numThreePower)
    
print(makeList)

mapList = list(map(powerByThree, myList))
mapListLambda = list(map(lambdaPowerByThree, myList))
mapListLambda2 = list(map(lambda num: num+10, myList))


print(mapList)
print(mapListLambda)
print(mapListLambda2)


# filter()


myList2 = [2, 3, 4, 5, 6, 7, 8]

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
lamdbdaIsEven = lambda n: True if n%2 == 0 else False    


isEvenList = list(filter(isEven, myList2))
isEvenList_lambda = list(filter(lamdbdaIsEven, myList2))
isEvenList_lambda2 = list(filter(lambda n: True if n%2 == 0 else False , myList2))

print(isEvenList)
print(isEvenList_lambda)
print(isEvenList_lambda2)



