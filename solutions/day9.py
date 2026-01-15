def day9():
    solve_for_b = True

    # grid = read_file("./data/day9_test.txt")  # 50, 24
    grid = read_file("./data/day9.txt")  # 4741848414
    if solve_for_b:
        outline = find_rect_outline(grid)
    else:
        outline = None
    find_max_rectangle(grid, outline)


def read_file(filepath: str) -> list[list[int]]:
    with open(filepath, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    positions = []
    for line in lines:
        pos = line.split(",")
        positions.append((int(pos[1]), int(pos[0])))  # convert to row,col format

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


def find_rect_outline(positions: list[list[int, int]]) -> set[tuple[int, int]]:
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

    return points


# position already sorted by row.
def find_max_rectangle(
    positions: list[tuple[int, int, int, int]],
    outline: set[tuple[int, int]] | None = None,
):
    rectangles: list[list[int, tuple[int, int]]] = []
    max_area = 0
    for i in range(len(positions) - 1):
        for j in range(i + 1, len(positions)):
            r0, c0 = positions[i]
            r1, c1 = positions[j]
            area = abs((r1 - r0 + 1) * (c1 - c0 + 1))

            # find the 4 corners
            ul = (min(r0, r1), min(c0, c1))
            ur = (max(r0, r1), min(c0, c1))
            bl = (min(r0, r1), max(c0, c1))
            br = (max(r0, r1), max(c0, c1))

            # this is for part-bn
            if outline:
                if (
                    ray_trace(ul, outline)
                    and ray_trace(ur, outline)
                    and ray_trace(bl, outline)
                    and ray_trace(br, outline)
                ):
                    rectangles.append([area, (ul, ur, bl, br)])
                    max_area = max(max_area, area)

    rectangles.sort(key=lambda x: x[0], reverse=True)
    for rect in rectangles:
        print(rect)

    print(f"max area: {max_area}")


# use ray-tracing to see if the point will intersect 4 sides of the outline.
def ray_trace(point: tuple[int, int], points: list[tuple[int, int]]) -> bool:
    points.sort(key=lambda x: x[0])
    min_row = points[0][0]
    max_row = points[-1][0]
    points.sort(key=lambda x: x[1])
    min_col = points[0][1]
    max_col = points[-1][1]

    row, col = point

    test_line = list(filter(lambda x: x[1] == col, points))
    # scan up
    # scan down

    test_line = list(filter(lambda x: x[0] == row, points))
    # scan right
    # scan left


if __name__ == "__main__":
    day9()
