def day10():
    problem_sets = read_file("./data/day10_test.txt")

    solve_a(problem_sets)


def solve_a(problem_sets):
    for prob in problem_sets[0:1]:
        target = prob[0]
        initial_state = [False for i in range(len(target))]
        target = prob[0]
        actions = [[3], [1, 3], [2]]  # prob[1]
        min_steps = exp(target=target, actions=actions, state=initial_state)
        print(f"min_steps = {min_steps}")


def exp(
    target,
    actions: list[list[int]],
    state: list[bool],
    last_action_idx=-1,
    depth=0,
    path: list[list[int]] = [],
):
    # target # [False,True,True,False]
    # actions  # [[3],[1,3],[2,3]]

    indent = "...." * (depth - 1)

    if last_action_idx >= 0:
        print(f"{indent}{actions[last_action_idx]} {state}")

    if target == state:
        print(f"!!!EXIT!!!{path} {depth+1}")
        return 1

    if depth > 4:
        return 5

    min_steps = 100000

    for i in range(len(actions)):
        if i == last_action_idx:
            continue
        new_state = perform_action(state, actions[i])
        path.append(actions[i])
        steps = 1 + exp(
            target,
            actions,
            new_state,
            last_action_idx=i,
            depth=depth + 1,
            path=path,
        )

        min_steps = min(min_steps, steps)

    return min_steps


def perform_action(state: list[bool], action_arr: list[int]) -> list[bool]:
    for action in action_arr:
        state[action] = not state[action]

    return state


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
