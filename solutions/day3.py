def day3():
    # solve("./data/day3_test.txt")  # 357, 3121910778619
    solve("./data/day3.txt")  # 11766


def solve(filepath: str):
    with open(filepath, "r") as file:
        rows = file.readlines()
        rows: list[str] = [row.strip() for row in rows]

    result = 0
    result2 = 0

    import time

    start_time = time.perf_counter()
    for row in rows:
        result += _findLargestPair(row)
        result2 += int(_findLargest12(row))

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time}")

    print(f"total joltage: {result}, {result2}")


def _findLargestPair(strValue: str) -> int:
    # print(f"find largest: {strValue}")
    if len(strValue) <= 1:
        return 0

    largestValue = -1
    idx1 = 0
    idx2 = 1
    maxTensValue = int(strValue[idx1])

    while idx1 < len(strValue) - 1:
        idx2 = idx1 + 1

        # don't bother to check if the tens value is lower
        if int(strValue[idx1]) < maxTensValue:
            idx1 += 1
            continue

        while idx2 < len(strValue):
            curValue = int(f"{strValue[idx1]}{strValue[idx2]}")
            if curValue > largestValue:
                largestValue = curValue
            idx2 += 1

        maxTensValue = int(strValue[idx1])
        idx1 += 1

    # print(f"largest value: {largestValue}")
    return largestValue


def _findLargest12(s: str, start=0, current=""):
    # # Base case: we've selected n characters
    # if len(current) == 12:
    #     return current

    # # Base case: not enough characters left
    # if start >= len(s):
    #     return "0"

    maxValueStr = "0"
    for i in range(start, len(s)):
        newStr = current + s[i]
        val = newStr
        if len(newStr) < 3:
            val = _findLargest12(s, i + 1, newStr)
        maxValueStr = str(max(int(maxValueStr), int(val)))

    return maxValueStr


# def _findLargest12(s: str, start=0, current=""):
#     # Base case: we've selected n characters
#     if len(current) == 12:
#         return current

#     # Base case: not enough characters left
#     if start >= len(s):
#         return "0"

#     maxValueStr = "0"
#     for i in range(start, len(s)):
#         # pre-check for optimization
#         newStr = current + s[i]
#         if len(maxValueStr) > 1:
#             count = len(newStr)
#             to_test_str = maxValueStr[0:count]
#             if int(to_test_str) >= int(newStr):
#                 continue

#         val = _findLargest12(s, i + 1, newStr)
#         maxValueStr = str(max(int(maxValueStr), int(val)))

#     print(f"largest value: {maxValueStr}")
#     return maxValueStr


if __name__ == "__main__":
    day3()
