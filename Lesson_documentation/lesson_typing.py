from typing import List

# Тип данных
number = 15 # int
# number = "10"
print(number + 12)

number: int = 15
name: str = "Askar"

tupleNames: tuple[int, int] = (12, 3)
mixedTuple: tuple[int, str] = (12, "Some")
tuple3: tuple[int, ...] = (12, 3, 43)

listNames: list[str] = ["Oscar", "Sam", "Adam"]
listNumbers: list[int] = [2134, 5, 54]
listNumbers: List[int] = [324, 43, 5]

dictContact: dict[str, str] = {
    "Adam": "+996 5551324545",
    "Peter": "+1423423452543"
}

numbers: set[int] = {12, 43, 54}
namesSet: set[str] = {"Tamara", "Marat"}


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 
        Function that returns list of numbers that can be added between each other 
        and give as a result of a target
        """

listPeopleWithProfessions: list[list[str, str], int] = [
    ["Adam", "Doctor"],
    ["Peter", "Firefighter"],
    ["Sam", "Engineer"],
    3
]
        





