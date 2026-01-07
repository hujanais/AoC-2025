def do_day1():
    # do_work("./data/day1_test.txt")  # returns 32, 3
    do_work("./data/day1.txt")  # final dial position: 70.  Password: 1147


def do_work(filepath: str):
    with open(filepath, "r") as file:
        lines_list = file.read().splitlines()

    # ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
    max_steps = 100
    dial_position = 50
    result = 0
    for step in lines_list:
        count = int(step[1:])
        prev_position = dial_position
        if step[0] == "L":
            dial_position = dial_position - count
        else:
            dial_position = dial_position + count

        # works for python only
        dial_position = dial_position % max_steps

        # in javascript, need a seperate operation.
        if dial_position < 0:
            dial_position += max_steps

        print(f"{step}, {prev_position} -> {dial_position}")
        if dial_position == 0:
            result += 1

    print(f"final dial position: {dial_position}.  Password: {result}")


if __name__ == "__main__":
    do_day1()
