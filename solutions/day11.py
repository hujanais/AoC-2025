def day11():
    # graph = build_graph("data/day11_test.txt") # 5
    # graph = build_graph("data/day11.txt")  # 603

    # start_state = "you"
    # num_of_paths = dfs(start_state, graph)
    # print(f"part-a: {num_of_paths}")

    graph = build_graph("data/day11b_test.txt")  # 2
    start_state = "svr"
    num_of_paths = dfs(start_state, graph)
    print(f"part-a: {num_of_paths}")


def dfs(state: str, graph, path=[], all_paths=[], memo=None):
    if memo is None:
        memo = {}

    path.append(state)

    if state == "out":
        all_paths.append(path)
        return (0, all_paths)

    if state in memo:
        return memo[state]

    neighbors = graph[state]
    counts = 0
    for neighbor in neighbors:
        counts, paths = dfs(neighbor, graph, path, all_paths, memo)
        counts += 1
    memo[state] = (counts, all_paths)
    return memo[state]


def build_graph(filepath: str):
    graph = {}
    with open(filepath, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    for line in lines:
        arr = line.split(":")
        graph[arr[0]] = arr[1].lstrip().split(" ")

    return graph


if __name__ == "__main__":
    day11()
