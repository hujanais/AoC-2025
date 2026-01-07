from pprint import pprint


def day4():
    print(solve("./data/day4_test.txt"))
    print(solve("./data/day4.txt"))


def solve(filepath: str) -> int:
    grid: list[list[int]] = []
    result = 0

    with open(filepath, "r") as file:
        lines = [line.strip() for line in file.readlines()]

        numRows = len(lines)
        numCols = len(lines[0])

        for row in range(numRows):
            rowArr = []
            for col in range(numCols):
                rowArr.append(lines[row][col])

            grid.append(rowArr)

        pprint(grid)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "@":
                if count_neighbors(grid, row, col) < 4:
                    result += 1

    return result


def count_neighbors(grid: list[list[int]], row, col) -> int:
    delta_arr = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    neighbors = 0

    for delta in delta_arr:
        new_row = row + delta[0]
        new_col = col + delta[1]

        if (
            new_row >= 0
            and new_row < len(grid)
            and new_col >= 0
            and new_col < len(grid[0])
            and grid[new_row][new_col] == "@"
        ):
            neighbors += 1

    return neighbors


if __name__ == "__main__":
    day4()
