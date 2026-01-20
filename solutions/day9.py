def day9():
    solve_for_b = True

    # grid = read_file("./data/day9_test.txt")  # 50, 24
    grid = read_file("./data/day9.txt")  # 4741848414, 4633585821(too high)
    # if solve_for_b:
    #     outline = find_rect_outline(grid)
    # else:
    #     outline = None
    # find_max_rectangle(grid, outline)


def read_file(filepath: str) -> list[list[int]]:
    with open(filepath, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    positions = []
    for line in lines:
        pos = line.split(",")
        positions.append((int(pos[1]), int(pos[0])))  # convert to row,col format

    # sort by rows
    positions.sort(key=lambda x: x[0])

    max_rows = max(positions, key=lambda x: x[0])[0]
    max_cols = max(positions, key=lambda x: x[1])[1]

    for position in positions:
        print(position)

    for row in range(max_rows):
        for col in range(max_cols):
            if (row, col) in positions:
                print("#", end="")
            else:
                print(".", end="")
        print()

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
    count = 122760

    # pre-sort once to optimize
    outline_sorted_by_rows = sorted(outline, key=lambda x: x[0])
    outline_sorted_by_cols = sorted(outline, key=lambda x: x[1])

    for i in range(len(positions) - 1):
        for j in range(i + 1, len(positions)):

            if count % 100 == 0:
                print(f"{count}")
            count -= 1
            r0, c0 = positions[i]
            r1, c1 = positions[j]
            area = abs((r1 - r0 + 1) * (c1 - c0 + 1))

            # find the 4 corners
            ul = (min(r0, r1), min(c0, c1))
            ur = (max(r0, r1), min(c0, c1))
            bl = (min(r0, r1), max(c0, c1))
            br = (max(r0, r1), max(c0, c1))

            # this is for part-b
            if outline:
                if (
                    ray_trace(ul, outline_sorted_by_rows, outline_sorted_by_cols)
                    and ray_trace(ur, outline_sorted_by_rows, outline_sorted_by_cols)
                    and ray_trace(bl, outline_sorted_by_rows, outline_sorted_by_cols)
                    and ray_trace(br, outline_sorted_by_rows, outline_sorted_by_cols)
                ):
                    # rectangles.append([area, (ul, ur, bl, br)]) # don't do this to save memory
                    max_area = max(max_area, area)
            else:
                rectangles.append([area, (ul, ur, bl, br)])
                max_area = max(max_area, area)

    rectangles.sort(key=lambda x: x[0], reverse=True)

    for rect in rectangles:
        print(rect)

    print(f"max area: {max_area}")


# use ray-tracing to see if the point will intersect 4 sides of the outline.
def ray_trace(
    point: tuple[int, int], outline_sorted_by_rows, outline_sorted_by_cols
) -> bool:
    row, col = point

    # test row
    test_line = list(filter(lambda x: x[1] == col, outline_sorted_by_rows))
    row_lowerbound, _ = test_line[0]
    row_upperbound, _ = test_line[-1]
    if row < row_lowerbound or row > row_upperbound:
        return False

    # test column
    test_line = list(filter(lambda x: x[0] == row, outline_sorted_by_cols))
    _, col_lowerbound = test_line[0]
    _, col_upperbound = test_line[-1]
    # scan right
    # scan left
    if col < col_lowerbound or col > col_upperbound:
        return False

    return True


if __name__ == "__main__":
    day9()
