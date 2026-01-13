def day9():
    # grid = read_data = read_file("./data/day9_test.txt") # 50
    grid = read_data = read_file("./data/day9.txt") # 4741848414
    find_max_rectangle(grid)

def read_file(filepath: str) -> list[list[int]]:
    with open(filepath, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    positions = []
    for line in lines:
        pos = line.split(",")
        positions.append((int(pos[1]), int(pos[0])))
    
    positions.sort(key=lambda x: x[0])

    max_rows = max(positions, key=lambda x: x[0])[0] + 2
    max_cols = max(positions, key=lambda x: x[1])[1] + 3

    # for position in positions:
    #     print(position)

    # for row in range(max_rows):
    #     for col in range(max_cols):
    #         if (row, col) in positions:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print()

    return positions

# position already sorted by row.
def find_max_rectangle(positions: list[tuple[int, int]]):
    max_area = 0
    for i in range(len(positions)-1):
        for j in range(i+1, len(positions)):
            x0, y0 = positions[i]
            x1, y1 = positions[j]
            area = abs((x1-x0+1)*(y1-y0+1))
            print(x0, y0, x1, y1, area)
            max_area = max(max_area, area)

    print(f"max area: {max_area}")


if __name__ == "__main__":
    day9()