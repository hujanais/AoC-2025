def do_day2():
    # do_work("./data/day2_test.txt")  # Result: 1227775554, 4174379265
    do_work("./data/day2.txt")  # Result: 18700015741, 20077272987


def do_work(filepath: str):
    ranges = []
    with open(filepath, "r") as file:
        content = file.read()
        ranges = content.split(sep=",")

    result: int = 0
    result2: int = 0
    for range in ranges:
        [startVal, endVal] = range.split("-")
        repeats_arr, repeats2_arr = find_repeats(int(startVal), int(endVal))

        result += sum(repeats_arr)
        result2 += sum(repeats2_arr)

    print(f"Result: {result}, {result2}")


def find_repeats(start: int, end: int) -> tuple[list[int], list[int]]:
    repeats_arr: list[int] = []
    repeats2_arr: list[int] = []
    while start <= end:
        if is_repeat(start):
            repeats_arr.append(start)
            # print(f"{start} is a repeat")

        if is_repeat2(str(start)):
            repeats2_arr.append(start)
            print(f"{start} is a repeat2")

        start += 1

    return (repeats_arr, repeats2_arr)


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
    # print("testing " + strValue)
    max_block_size = int(len(strValue) / 2) + 1
    block_set: set = set()
    for block_size in range(1, max_block_size):
        i = 0
        block_set.clear()
        while i < len(strValue):
            j = i + block_size
            block_set.add(strValue[i : j])
            i = i + block_size

            if len(block_set) > 1:
                break

        if len(block_set) == 1:
            return True

    return False


if __name__ == "__main__":
    do_day2()
    # is_repeat2("12211221")
