def do_day2():
    # do_work("./data/day2_test.txt")  # Result: 1227775554
    do_work("./data/day2.txt")  # Result: 18700015741


def do_work(filepath: str):
    ranges = []
    with open(filepath, "r") as file:
        content = file.read()
        ranges = content.split(sep=",")

    result: int = 0
    for range in ranges:
        [startVal, endVal] = range.split("-")
        repeats_arr = find_repeats(int(startVal), int(endVal))

        for val in repeats_arr:
            result += val

    print(f"Result: {result}")


def find_repeats(start: int, end: int) -> list[int]:

    repeats_arr: list[int] = []
    while start <= end:
        if is_repeat(start):
            repeats_arr.append(start)
            print(f"{start} is a repeat")

        start += 1

    return repeats_arr


def is_repeat(value: int) -> bool:
    strValue = str(value)

    # exit if string len is odd.
    strLen = len(strValue)
    if strLen % 2 != 0:
        return False

    firstIdx = 0
    midIdx = int(strLen / 2)
    secondIdx = midIdx

    while firstIdx < midIdx:
        if strValue[firstIdx] != strValue[secondIdx]:
            return False
        firstIdx += 1
        secondIdx += 1

    return True


if __name__ == "__main__":
    do_day2()
