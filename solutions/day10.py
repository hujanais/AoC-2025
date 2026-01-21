def day10():
    # problem_sets = read_file("./data/day10_test.txt")
    problem_sets = read_file(
        "./data/day10.txt"
    )  # 422 had to run row 66 with depth of 10.
    # solve_a(problem_sets)
    solve_b(problem_sets)


def solve_a(problem_sets):
    result = 0
    idx = 0
    for prob in problem_sets:
        target = prob[0]
        initial_state = [False for i in range(len(target))]
        target = prob[0]
        actions = prob[1]
        min_steps, shortest_path = exp(
            target=target, actions=actions, state=initial_state
        )
        print(f"{idx} min_steps = {min_steps}, path = {shortest_path}")
        result += min_steps
        idx += 1
    print(f"result = {result}")


def solve_b(problem_sets):
    result = 0
    idx = 0
    for prob in problem_sets[0:1]:
        target = prob[0]
        initial_state = [0 for i in range(len(target))]
        actions = prob[1]
        joltage_target = list(
            map(lambda x: int(x), prob[2].replace("{", "").replace("}", "").split(","))
        )
        min_steps, shortest_path = bfs(
            target=joltage_target, actions=actions, state=initial_state
        )
        print(f"{idx} min_steps = {min_steps}, path = {shortest_path}")
        result += min_steps
        idx += 1
    print(f"result-b = {result}")


def exp(
    target,
    actions: list[list[int]],
    state: list[bool],
    last_action_idx=-1,
    depth=0,
    path: list[list[int]] | None = None,
    dp=None,
):
    if path is None:
        path = []
    # target # [False,True,True,False]
    # actions  # [[3],[1,3],[2,3]]

    if dp is None:
        dp = {}

    key = (tuple(state), last_action_idx, depth)
    if key in dp:
        return dp[key]

    indent = "." * (depth - 1)

    path_set = set(tuple(inner_list) for inner_list in path)
    if len(path_set) != len(path):
        return (100000, None)

    if target == state:
        return (0, path.copy())

    # prevent infinite loop
    if depth > 7:
        return (100000, None)

    min_steps = 100000
    best_path = None

    for i in range(len(actions)):
        if i == last_action_idx:
            continue
        new_state, _ = perform_action(state, actions[i], None)
        path.append(actions[i])

        if len(path) > min_steps:
            # print("skip")
            steps = 1000
        else:
            steps, sub_path = exp(
                target,
                actions,
                new_state,
                last_action_idx=i,
                depth=depth + 1,
                path=path,
                dp=dp,
            )
            steps += 1

        if steps < min_steps:
            min_steps = steps
            best_path = sub_path.copy() if sub_path else None

        path.pop()  # Backtrack: remove the action we just tried

    dp[key] = (min_steps, best_path)
    return (min_steps, best_path)


def bfs(
    target: list[int],
    actions: list[list[int]],
    state: list[int],
    depth=0,
    path: list[list[int]] | None = None,
    dp=None,
):
    if path is None:
        path = []

    if dp is None:
        dp = {}

    key = (tuple(state), depth)
    if key in dp:
        return dp[key]

    if target == state:
        return (0, path.copy())

    target_sum = sum(target)
    current_sum = sum(state)
    if current_sum > target_sum:
        print(f"skip. {current_sum} > {target_sum}")
        return (100000, None)

    # prevent infinite loop
    if depth > 20:
        return (100000, None)

    min_steps = 100000
    best_path = None

    for i in range(len(actions)):
        _, new_joltage = perform_action(state, actions[i], state)
        path.append(actions[i])

        if depth > min_steps:
            # print(f"skip. {depth} > {min_steps}")
            steps = 1000
        else:
            steps, sub_path = bfs(
                target=target,
                actions=actions,
                state=new_joltage,
                depth=depth + 1,
                path=path,
                dp=dp,
            )
            steps += 1

        if steps < min_steps:
            min_steps = steps
            best_path = sub_path.copy() if sub_path else None

        path.pop()  # Backtrack: remove the action we just tried

    dp[key] = (min_steps, best_path)
    return (min_steps, best_path)


def perform_action(
    state: list[bool], action_arr: list[int], joltage_input: list[int] = None
) -> tuple[list[bool], list[int]]:
    # Create a copy to avoid mutating the original state
    new_state = state.copy()
    joltages = joltage_input.copy() if joltage_input else None

    for action in action_arr:
        new_state[action] = not new_state[action]
        if joltage_input:
            joltages[action] += 1

    return new_state, joltages


def read_file(filepath: str):
    lines = []
    with open(filepath, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    problem_sets = []
    for line in lines:
        arr = line.split()
        output_str = arr[0]
        output_str = output_str.removeprefix("[").removesuffix("]")
        output_arr = [True if c == "#" else False for c in output_str]

        action_instructions = []
        actions = arr[1:-1]
        for action in actions:
            action = action.removeprefix("(").removesuffix(")").split(",")
            action_arr = [int(c) for c in action]
            action_instructions.append(action_arr)

        extra = arr[-1]

        problem_sets.append((output_arr, action_instructions, extra))

    return problem_sets


if __name__ == "__main__":
    day10()
