from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass
class IdRange():
    startIdx: int = 0
    endIdx: int = 0

    def __init__(self, startIdx: int, endIdx: int):
        self.startIdx = startIdx
        self.endIdx = endIdx

    def inRange(self, value: int):
        return value >= self.startIdx and value <= self.endIdx
    
    def isRangeOverlapped(self, input_range: IdRange):
        return self.inRange(input_range.startIdx) or self.inRange(input_range.endIdx)

def day5():
    # day5_test.txt -> 3, 14
    # day5.txt -> 773

    with open("./data/day5_test.txt", 'r') as f: 
        lines = list(map(lambda x: x.strip() ,f.readlines()))
    
    fresh_list: list[IdRange] = []
    ingredients: list[int] = []
    for line in lines:
        if '-' in line:
            items = line.split('-')
            startIdx = int(items[0])
            endIdx = int(items[1])
            fresh_list.append(IdRange(startIdx=startIdx, endIdx=endIdx))
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
    nMaxFreshItems = 0
    merged_list = range_union(fresh_list=fresh_list)
    for item in merged_list:
        nMaxFreshItems += item.endIdx - item.startIdx + 1

    return nFreshItems, nMaxFreshItems

def range_union(fresh_list: list[IdRange]) -> list[IdRange]:
    # step 1. sort the list.
    fresh_list.sort(key=lambda x: x.startIdx)
    new_list: list[IdRange] = [fresh_list[0]]
    for item in fresh_list[1:]:
        new_item = new_list[len(new_list) - 1]
        if item.isRangeOverlapped(new_item):
            new_list.append(IdRange(new_item.startIdx, new_item.endIdx))
        else:
            new_list.append(item)
        
    print(new_list)
    return new_list

        


if __name__ == "__main__":
    day5()