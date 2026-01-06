def do_day2():
    do_work("./data/day2_test.txt")  # returns 32, 3
    # do_work("./data/day1.txt")  # final dial position: 70.  Password: 1147


def do_work(filepath: str):
    ranges = []
    with open(filepath, "r") as file:
        content = file.read()
        ranges = content.split(sep=",")

    for range in ranges:
        find_repeats(range)


def find_repeats(range: str):
    startVal = 0
    endVal = 0

    while startVal <= endVal:
        if is_repeat(startVal):
            print(f"{startVal} is a repeat")

        startVal += 1


def is_repeat(value: int) -> bool:
    return False
