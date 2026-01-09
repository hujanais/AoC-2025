import pandas as pd


def day6(filepath: str):
    solve(filepath)
    solve2(filepath)


def solve(filepath: str):
    table_df = pd.read_table(filepath, sep="\\s+", header=None)
    nCols = len(table_df.columns)
    result = 0
    for i in range(0, nCols):
        col: pd.Series = table_df[i]
        values: list[int] = [int(value) for value in col[:-1].values]
        operator = col[-1:].values[0]
        result += calculate(values, operator)

    print(result)


def solve2(filepath: str):
    lines = []
    with open(
        filepath,
        "r",
    ) as f:
        lines = [line.strip("\n") for line in f.readlines()]

    nCols = len(lines[0])
    nRows = len(lines)

    result = 0
    operators: list[str] = lines[-1].split()
    numbers: list[str] = []
    block = 0
    for c in range(nCols):
        strVal = ""
        delimiter = True
        for r in range(nRows - 1):  # don't bother with the operator line
            if lines[r][c] != " ":
                strVal += lines[r][c]
                delimiter = False
        if delimiter:
            result += calculate(list(map(lambda x: int(x), numbers)), operators[block])
            numbers.clear()
            block += 1
        else:
            numbers.append(strVal)

    # handle the last item.
    result += calculate(list(map(lambda x: int(x), numbers)), operators[block])

    print(result)


def calculate(values: list[int], operator: str) -> float:
    result = values[0]
    for value in values[1:]:
        if operator == "+":
            result += value
        elif operator == "*":
            result *= value
        else:
            raise Exception("invalid operator")

    return result


if __name__ == "__main__":
    # day6("./data/day6_test.txt")  # 4277556, 3263827
    day6("./data/day6.txt")  # 5316572080628, 11299263623062
