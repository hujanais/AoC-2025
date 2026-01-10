from functools import total_ordering


def day7():
    # solve_a('./data/day7_test.txt') # 21
    # solve_a('./data/day7.txt') # 1537
    # solve_b('./data/day7_test.txt') # 40
    solve_b('./data/day7.txt') # 18818811755665
def solve_a(filepath: str):
    with open(filepath, 'r') as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))

    grid: list[list[str]] = build_grid(lines)
    # find the starting point 'S'
    startCol = [0, grid[0].index('S')]

    tachyons = []
    tachyons.append(startCol)
    new_tachyons = set[tuple[int, int]]()

    total_splits = 0
    splits = 0
    nRows = len(grid)
    for i in range(nRows - 1):
        new_tachyons.clear()
        splits = 0
        for item in tachyons:
            new_row = item[0] + 1
            new_col = item[1]
            if grid[new_row][new_col] == '.':
                grid[new_row][new_col] = '*'
                new_tachyons.add((new_row, new_col))
            elif grid[new_row][new_col] == '^':
                splits += 1
                if grid[new_row][new_col-1] == '.' or grid[new_row][new_col-1] == '*':
                    grid[new_row][new_col-1] = '|'
                    new_tachyons.add((new_row, new_col-1))
                if grid[new_row][new_col+1] == '.' or grid[new_row][new_col+1] == '*':
                    grid[new_row][new_col+1] = '|'
                    new_tachyons.add((new_row, new_col+1))

        total_splits += splits
        # update tachyons array
        tachyons = [t for t in new_tachyons]

        # replace '*' with '|' for visualization only
        grid[new_row] = ['|' if p == '*' else p for p in grid[new_row]]
        if splits > 0:
            print(f"-----{splits}-----")
            for line in grid:
                print(line)

    print(f"Total splits: {total_splits}")

def solve_b(filepath: str):
    with open(filepath, 'r') as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))

    grid: list[list[str]] = build_grid(lines)
    # find the starting point 'S'
    startCol = [0, grid[0].index('S')]

    total_paths = dfs(grid, position = startCol)
    print(f"Total Paths: {total_paths}")

# find all paths
def dfs(grid: list[list[str]], position: list[int, int], dp: dict[str, int] = dict()) -> int:
    endRow = len(grid) - 1
    
    # out of bounds
    if position[1] < 0 or position[1] >= len(grid[0]):
        return 0
    
    # end-point
    if position[0] == endRow:
        return 1
    
    row = position[0]
    col = position[1]

    key = f"{row}-{col}" 
    if key in dp:
        return dp[key]

    paths = 0
    if grid[row+1][col] == '.':
        paths += dfs(grid, [row+1, col])
    else:
        # move left
        paths += dfs(grid, [row+1, col-1])
        # move right
        paths += dfs(grid, [row+1, col+1])

    dp[key] = paths
    return paths

def build_grid(lines: str) -> list[list[str]]:
    rows = len(lines)
    cols = len(lines[0])

    grid = [[lines[r][c] for c in range(cols)] for r in range(rows)]
    for line in grid:
        print(line)

    return grid

if __name__ == "__main__":
    day7()