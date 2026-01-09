import time

def day3():
    solve("./data/day3_test.txt")  # 357, 3121910778619
    # solve("./data/day3.txt")  # 17766, 176582889354075 This is very slow. many minutes!

def solve(filepath: str):
    with open(filepath, "r") as file:
        rows = file.readlines()
        rows: list[str] = [row.strip() for row in rows]

    result = 0
    result2 = 0
    for row in rows:
        result += _findLargestPair(row)
        result2 += int(_findLargest12(row))
        print(f"- {result} {result2}")

    print(f"{result}, {result2}")

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
    maxValueStr = "0"
    for i in range(start, len(s)):
        newStr = current + s[i]
        val = newStr
        if len(newStr) < 12:
            count = len(newStr)
            maxValue = int(maxValueStr[0:count])
            if int(newStr) > maxValue:
                val = _findLargest12(s, i + 1, newStr)
        maxValueStr = str(max(int(maxValueStr), int(val)))

    return maxValueStr

if __name__ == "__main__":
    day3()
    # start_time = time.perf_counter()
    # # print(_findLargestPair("731122458443"))
    # print(_findLargest12("6739459674389333459433695375559949344734767926833587823236783998689734978783695374574455875833736627"))
    # end_time = time.perf_counter()
    # elapsed_time = end_time - start_time
    # print(f"Elapsed Time: {elapsed_time}")