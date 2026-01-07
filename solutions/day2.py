def do_day2():
    do_work("./data/day2_test.txt")  # Result: 1227775554
    # do_work("./data/day2.txt")  # Result: 18700015741


def do_work(filepath: str):
    ranges = []
    with open(filepath, "r") as file:
        content = file.read()
        ranges = content.split(sep=",")

    result: int = 0
    for range in ranges:
        [startVal, endVal] = range.split("-")
        repeats_arr = find_repeats(int(startVal), int(endVal))

        result += sum(repeats_arr)

    print(f"Result: {result}")


def find_repeats(start: int, end: int) -> list[int]:
    repeats_arr: list[int] = []
    while start <= end:
        # if is_repeat(start):
        #     repeats_arr.append(start)
        #     print(f"{start} is a repeat")

        if is_repeat2(str(start)):
            print(f"{start} is a repeat2")

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


def is_repeat2(strValue: str, block_size: int = 1) -> bool:
    print("testing " + strValue)
    max_block_size = int(len(strValue) / 2) + 1
    block_set: set = set()
    for block_size in range(1, max_block_size):
        i = 0
        while i < len(strValue):
            block_set.add(strValue[i : i + block_size])
            i = i + block_size

        if len(block_set) == 1:
            return True

    return False


if __name__ == "__main__":
    do_day2()
