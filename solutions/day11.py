def day11():
    lines = []
    graph = {}
    with open("data/day11_test.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    for line in lines:
        arr = line.split(":")
        graph[arr[0]] = arr[1].lstrip().split(" ")

    print(graph)


if __name__ == "__main__":
    day11()
