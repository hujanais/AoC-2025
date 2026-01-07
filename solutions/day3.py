def day3():
    solve("./data/day3_test.txt")  # 98 + 89 + 78 + 92 = 357
    solve("./data/day3.txt")  # 11766


def solve(filepath: str):
    with open(filepath, "r") as file:
        rows = file.readlines()
        rows: list[str] = [row.strip() for row in rows]

    result = 0
    for row in rows:
        result += _findLargestPair(row)

    print(f"total joltage: {result}")


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


def dp(strValue: str, idx1: int, idx2: int) -> int | None:
    strLen = len(strValue)

    # Base cases
    if strLen <= 1:
        return None


if __name__ == "__main__":
    day3()
