from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass
class IdRange():
    startIdx: int = 0
    endIdx: int = 0

    def __init__(self, range_input: str):
        items = range_input.split('-')
        self.startIdx = int(items[0])
        self.endIdx = int(items[1])

    def inRange(self, value: int):
        return value >= self.startIdx and value <= self.endIdx
    
    def isRangeOverlapped(self, input_range: IdRange):
        return self.inRange(input_range.startIdx) or self.inRange(input_range.endIdx)

def day5():
    # day5_text.txt -> 3, 14
    # day5.txt -> 773

    with open("./data/day5.txt", 'r') as f: 
        lines = list(map(lambda x: x.strip() ,f.readlines()))
    
    fresh_list: list[IdRange] = []
    ingredients: list[int] = []
    for line in lines:
        if '-' in line:
            fresh_list.append(IdRange(line))
        elif len(line) > 0:
            ingredients.append(int(line))

    result1, result2 = solve(fresh_list, ingredients)
    print(result1, result2)

def solve(fresh_list: list[IdRange], ingredients: list[int]) -> tuple[int, int]:
    # part a
    nFreshItems = 0
    for ingredient in ingredients:
        for fresh in fresh_list:
            if fresh.inRange(ingredient):
                nFreshItems += 1
                break
            
    # part b
    # union the ranges

    return nFreshItems, 0

def range_union(fresh_list: list[IdRange]):
    
    for i in range(1, len(fresh_list)):
        reference = fresh_list[i-1]
        current = fresh_list[i]

        


if __name__ == "__main__":
    day5()