from __future__ import annotations
from dataclasses import dataclass


@dataclass
class IdRange:
    startIdx: int = 0
    endIdx: int = 0

    def __init__(self, startIdx: int, endIdx: int):
        self.startIdx = startIdx
        self.endIdx = endIdx

    def inRange(self, value: int):
        return value >= self.startIdx and value <= self.endIdx

    def isRangeOverlapped(self, input_range: IdRange):
        return (
            self.startIdx <= input_range.endIdx and self.endIdx >= input_range.startIdx
        )

    def __repr__(self):
        return f"{self.startIdx} - {self.endIdx}"


def day5():
    # result1, result2 = solve("./data/day5_test.txt")  #  -> 3, 14
    result1, result2 = solve("./data/day5.txt")  # -> 773 : 332067203034711
    print(result1, result2)


def solve(filepath: str) -> tuple[int, int]:
    with open(filepath, "r") as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))

    fresh_list: list[IdRange] = []
    ingredients: list[int] = []
    for line in lines:
        if "-" in line:
            items = line.split("-")
            startIdx = int(items[0])
            endIdx = int(items[1])
            fresh_list.append(IdRange(startIdx=startIdx, endIdx=endIdx))
        elif len(line) > 0:
            ingredients.append(int(line))

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
    # sort by start index and then check for overlap.
    # if no overlap, then add a new range
    # if overlap, update the range
    fresh_list = fresh_list
    fresh_list.sort(key=lambda x: x.startIdx)
    merged_list: list[IdRange] = [fresh_list[0]]
    for item in fresh_list[1:]:
        merge_item = merged_list[len(merged_list) - 1]
        if item.isRangeOverlapped(merge_item):
            merge_item.endIdx = max(item.endIdx, merge_item.endIdx)
        else:
            merged_list.append(item)

    # print(merged_list)
    return merged_list


if __name__ == "__main__":
    day5()
