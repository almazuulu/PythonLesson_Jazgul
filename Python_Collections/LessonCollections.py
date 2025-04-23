from collections import deque, defaultdict, OrderedDict, namedtuple

# deque (Двухсторонняя очередь)

namesList = ["Adam", "Peter", "David"]

namesList.append("Sam")
print(namesList)

namesList.insert(0, "Rinat")
print(namesList)

# Добавление и Удаление элементов спереди и с конца
d = deque()
d.append(1)  # добавление элемента назад
d.appendleft(4) # добавление элемента вперед
print(d)
print(d[0])
d[1] = 23
print(d)
d.append(232)
d.append(23)
d.append(56)
d = list(d)
print(d)
print(d[-3:])

k = deque()
k.append(76)
k.append(65)
k.append(12)
k.append(5)
k.appendleft(100)

print(k)

# Удаление элемента с конца
k.pop()
print(k)

# Удаление элемента спереди
k.popleft()
print(k)

# defaultdict - словарь по умолчанию
namesDict = {
    "Father": "03234234324",
    "Mother": "0342342343244",
    "Kanat": "03123123"
}

print(namesDict["Father"])
# print(namesDict["Timur"])

print(namesDict.get("Timur", "Нет такого контакта"))

ddict = defaultdict(int) # по умолчанию
print(ddict["a"])
print(ddict)
ddict["b"] += 1
print(ddict)
ddict["c"] = 3
print(ddict)
print(ddict["d"])
print(ddict)

busketList = defaultdict(list) # значения списки
busketList['fruits'].append('apple')
busketList['fruits'].append('banana')
busketList['fruits'].append('water melon')

busketList['others'].append('meat')
busketList['others'].append('eggs')
busketList['others'].append('milk')

print(busketList)

# OrderedDict()
oDict = OrderedDict()
oDict["one"] = 1
oDict["two"] = 2
oDict["three"] = 3


for k, v in oDict.items():
    print(k, v)


# namedtuple - кортежи с именованными полями почти как Классы - но легче

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)
print(p)

tupleInfo = ("Jazgul", 24, "Kyrgyzstan")
print(tupleInfo[0])
print(tupleInfo[2])


User = namedtuple("User", ["name", "age", "country"])
user1 = User("Jazgul", 24, "Kyrgyzstan")
print(user1.name)
print(user1.age)
print(type(user1))

print(user1)

user1.name = "Aselya"
print(user1.name)



