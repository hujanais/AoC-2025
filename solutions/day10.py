def day10():
    # problem_sets = read_file("./data/day10_test.txt")
    problem_sets = read_file("./data/day10.txt") # 432 too high
    solve_a(problem_sets)


def solve_a(problem_sets):
    result = 0
    idx = 0
    for prob in problem_sets:
        target = prob[0]
        initial_state = [False for i in range(len(target))]
        target = prob[0]
        actions = prob[1]
        min_steps, shortest_path = exp(target=target, actions=actions, state=initial_state)
        print(f"{idx} min_steps = {min_steps}, path = {shortest_path}")
        result += min_steps
        idx += 1
    print(f"result = {result}")

def exp(
    target,
    actions: list[list[int]],
    state: list[bool],
    last_action_idx=-1,
    depth=0,
    path: list[list[int]] | None = None,
):
    if path is None:
        path = []
    # target # [False,True,True,False]
    # actions  # [[3],[1,3],[2,3]]

    indent = "." * (depth - 1)

    if target == state:
        # print(f"##{indent}{path}")
        return (0, path.copy())

    # prevent infinite loop
    if depth > 5:
        return (100000, None)

    min_steps = 100000
    best_path = None

    for i in range(len(actions)):
        if i == last_action_idx:
            continue
        new_state = perform_action(state, actions[i])
        path.append(actions[i])
        steps, sub_path = exp(
            target,
            actions,
            new_state,
            last_action_idx=i,
            depth=depth + 1,
            path=path,
        )
        steps += 1
        if steps < min_steps:
            min_steps = steps
            best_path = sub_path.copy() if sub_path else None
        
        path.pop()  # Backtrack: remove the action we just tried

    return (min_steps, best_path)


def perform_action(state: list[bool], action_arr: list[int]) -> list[bool]:
    # Create a copy to avoid mutating the original state
    new_state = state.copy()
    for action in action_arr:
        new_state[action] = not new_state[action]

    return new_state


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
