def day10():
    # problem_sets = read_file("./data/day10_test.txt")
    problem_sets = read_file(
        "./data/day10.txt"
    )  # 422 had to run row 66 with depth of 10.

    solve_a(problem_sets)  # 7,
    # solve_b(problem_sets)  # 33


def solve_a(problem_sets):
    result = 0
    idx = 0
    for prob in problem_sets[66:67]:
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
    print(f"result a = {result}")


def solve_b(problem_sets):
    result = 0
    idx = 0
    for prob in problem_sets[0:1]:
        target = prob[0]
        initial_state = [False for i in range(len(target))]
        initial_joltages = [0 for i in range(len(target))]
        target = prob[0]
        actions = prob[1]
        joltage_str = prob[2].replace("{", "").replace("}", "")
        joltage_target = list(map(lambda x: int(x), joltage_str.split(",")))

        min_steps = exp_b(
            joltage_target=joltage_target,
            actions=actions,
            joltages=initial_joltages,
            state=initial_state,
        )
        print(f"{idx} min_steps = {min_steps}")
        result += min_steps
        idx += 1
    print(f"result b = {result}")


def exp(
    target,
    actions: list[list[int]],
    state: list[bool],
    last_action_idx=-1,
    depth=0,
    path: list[list[int]] | None = None,
    memo=None,
):
    if path is None:
        path = []
    # target # [False,True,True,False]
    # actions  # [[3],[1,3],[2,3]]

    indent = "." * (depth - 1)

    if memo is None:
        memo = {}

    key = tuple(state)
    # if key in memo:
    #     return memo[key]

    path_set = set(tuple(inner_list) for inner_list in path)
    if len(path_set) != len(path):
        # print("redundant path")
        return (100000, None)

    if target == state:
        # print(f"##{indent}{path}")
        return (0, path.copy())

    # prevent infinite loop
    if depth > 10:
        return (100000, None)

    min_steps = 100000
    best_path = None

    for i in range(len(actions)):
        if i == last_action_idx:
            continue
        new_state, new_joltages = perform_action(state, actions[i], joltage_input=None)
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
                memo=memo,
            )
            steps += 1

        if steps < min_steps:
            min_steps = steps
            best_path = sub_path.copy() if sub_path else None

        path.pop()  # Backtrack: remove the action we just tried

    memo[key] = (min_steps, best_path)
    return (min_steps, best_path)


def exp_b(
    joltage_target: list[int],
    actions: list[list[int]],
    joltages: list[int],
    state: list[bool],
    idx: int = 0,
    depth=0,
    dp=None,
):
    # target # [False,True,True,False]
    # actions  # [[3],[1,3],[2,3]]

    indent = "." * (depth - 1)

    if dp is None:
        dp = {}

    key = tuple(joltages)
    if key in dp:
        return dp[key]

    if depth > 50:  # Adjust based on problem constraints
        return 100000

    if joltages == joltage_target:
        print("done")
        return 0

    if any(a > b for a, b in zip(joltages, joltage_target)):
        return 100000

    print(f"{indent} {actions[idx]}")

    # prevent infinite loop
    if depth > 11:
        return 100000

    min_steps = 100000

    for i in range(len(actions)):
        new_state, new_joltages = perform_action(
            state, actions[i], joltage_input=joltages
        )

        steps = exp_b(
            joltage_target,
            actions,
            new_joltages,
            new_state,
            i,
            depth=depth + 1,
            dp=dp,
        )
        steps += 1

        if steps < min_steps:
            min_steps = steps

    dp[key] = min_steps
    return min_steps


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
