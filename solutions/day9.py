def day9():
    grid = read_data = read_file("./data/day9_test.txt")  # 50
    # grid = read_file("./data/day9.txt")  # 4741848414
    reds = find_all_reds(grid)
    find_max_rectangle(grid, reds)


def read_file(filepath: str) -> list[list[int]]:
    with open(filepath, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    positions = []
    for line in lines:
        pos = line.split(",")
        positions.append((int(pos[1]), int(pos[0])))

    positions.sort(key=lambda x: x[0])

    # max_rows = max(positions, key=lambda x: x[0])[0]
    # max_cols = max(positions, key=lambda x: x[1])[1]

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


def find_all_reds(positions: list[list[int, int]]) -> set[tuple[int, int]]:
    # Build outline
    points: list[tuple[int, int]] = []
    for i in range(len(positions) - 1):
        for j in range(i + 1, len(positions)):
            row0, col0 = positions[i]
            row1, col1 = positions[j]

            if row0 == row1:
                for col in range(min(col0, col1), max(col0, col1) + 1):
                    points.append((row0, col))
            elif col0 == col1:
                for row in range(min(row0, row1), max(row0, row1)):
                    points.append((row, col0))

    # Fill the space
    total_loops = len(points) ** 2
    reds: set[tuple[int, int]] = set()
    for i in range(len(points) - 1):
        total_loops -= 1
        if total_loops % 500 == 0:
            print(total_loops)
        for j in range(i + 1, len(points)):
            r0, c0 = points[i]
            r1, c1 = points[j]

            if r0 == r1:
                for col in range(min(c0, c1), max(c0, c1) + 1):
                    reds.add((r0, col))
            elif c0 == c1:
                for row in range(min(r0, r1), max(r0, r1)):
                    reds.add((row, c0))

    return reds


# position already sorted by row.
def find_max_rectangle(
    positions: list[tuple[int, int]], reds: set[tuple[int, int]] | None = None
):
    max_area = 0
    for i in range(len(positions) - 1):
        for j in range(i + 1, len(positions)):
            x0, y0 = positions[i]
            x1, y1 = positions[j]
            area = abs((x1 - x0 + 1) * (y1 - y0 + 1))

            # this is for part-bn
            if reds:
                # find the 4 corners
                ul = (min(x0, x1), min(y0, y1))
                ur = (max(x0, x1), min(y0, y1))
                bl = (min(x0, x1), max(y0, y1))
                br = (max(x0, x1), max(y0, y1))

                corners = {ul, ur, bl, br}
                if any(corner not in reds for corner in corners):
                    continue

            max_area = max(max_area, area)

    print(f"max area: {max_area}")


if __name__ == "__main__":
    day9()
