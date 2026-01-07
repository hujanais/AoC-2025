import math


def do_day1():
    # do_work("./data/day1_test.txt")  # returns 32, 3 | 6
    do_work(
        "./data/day1.txt"
    )  # final dial position: 70.  Password1: 1147, Password2: 6789


def do_work(filepath: str):
    with open(filepath, "r") as file:
        lines_list = file.read().splitlines()

    brute_force(lines_list)
    # optimized_solution(lines_list)


def optimized_solution(lines_list: list[str]):
    # ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    max_steps = 100
    dial_position = 50
    prev_position = dial_position
    result = 0
    result2 = 0

    for step in lines_list:
        count = int(step[1:])
        if step[0] == "L":
            dial_position = dial_position - count
        else:
            dial_position = dial_position + count

        # number of rotations
        rotations = 0
        if dial_position < 0:
            rotations = int(abs(dial_position / max_steps)) + 1
        else:
            rotations = int(abs(dial_position / max_steps))

        # works for python only
        dial_position = dial_position % max_steps

        # in javascript, need a seperate operation.
        if dial_position < 0:
            dial_position += max_steps

        if dial_position == 0:
            result += 1

        if dial_position == 0 and rotations > 0:
            rotations -= 1

        print(f"{step}, {prev_position} -> {dial_position}. rotations: {rotations}")

        result2 += rotations
        prev_position = dial_position

    print(
        f"final dial position: {dial_position}.  Password1: {result}, Password2: {result2}"
    )


def brute_force(lines_list: list[str]):
    position = 50
    hit_zero = 0
    at_zero = 0
    for step in lines_list:
        count = int(step[1:])
        delta = 0
        if step[0] == "L":
            delta = -1
        else:
            delta = 1

        for i in range(count):
            position += delta
            if position == -1:
                position = 99
            elif position == 100:
                position = 0

            if position == 0:
                hit_zero += 1

        if position == 0:
            at_zero += 1

    print(
        f"final dial position: {position}.  Password1: {at_zero}, Password2: {hit_zero}"
    )


if __name__ == "__main__":
    do_day1()

# The dial starts by pointing at 50.
# The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
# The dial is rotated L30 to point at 52.
# The dial is rotated R48 to point at 0.
# The dial is rotated L5 to point at 95.
# The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
# The dial is rotated L55 to point at 0.
# The dial is rotated L1 to point at 99.
# The dial is rotated L99 to point at 0.
# The dial is rotated R14 to point at 14.
# The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
