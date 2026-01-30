import re


def day12():
    toys, boxes = read_input("data/day12_test.txt")

    solve_a(toys, boxes[0])


def solve_a(toys, box):
    box_length, box_width, toy_counts = box

    box = [["." for _ in range(box_width)] for _ in range(box_length)]

    toy = toys[4]
    

    for line in box:
        print("".join(line))


def read_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    # only 5 toys.
    i = 0
    toys = []
    toy: list[list[str]] | None = None
    for line in lines[:30]:
        if i % 5 == 0:
            toy = []
        else:
            if line:
                toy.append(line)
            else:
                toys.append(toy)
        i += 1

    boxes = []
    for line in lines[30:]:
        digits_str = re.findall(r"\d+", line)
        length = int(digits_str[0])
        width = int(digits_str[1])
        toy_counts = [int(d) for d in digits_str[2:]]

        boxes.append((length, width, toy_counts))

    return (toys, boxes)


if __name__ == "__main__":
    day12()
