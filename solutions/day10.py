from collections import deque


def day10():
    # problem_sets = read_file("./data/day10_test.txt")
    problem_sets = read_file(
        "./data/day10.txt"
    )  # 422 had to run row 66 with depth of 10.

    # solve_a(problem_sets)  # 7,
    solve_b(problem_sets)  # 33


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

    for prob in problem_sets:
        actions = prob[1]
        joltage_target = list(
            map(lambda x: int(x), prob[2].replace("{", "").replace("}", "").split(","))
        )

        # find the first action that has a unique index
        indices = {}
        pre_count = 0
        for i in range(len(actions)):
            action = actions[i]
            for act in action:
                key = str(act)
                if key in indices:
                    count, idx = indices[key]
                    indices[key] = (count + 1, idx)
                else:
                    indices[key] = (1, i)

        for key, value in indices.items():
            if value[0] == 1:
                # apply action[value[1]]
                preapply_action = actions[action[1]]

                while all([x > 0 for x in joltage_target]):
                    pre_count += 1
                    _, joltage_target = perform_action(
                        joltage_target, preapply_action, joltage_target
                    )

                break

        min_steps, shortest_path = bfs(initial_state=joltage_target, actions=actions)
        print(
            f"{idx} min_steps = {min_steps} pre-steps={pre_count}, path = {shortest_path}"
        )
        result += min_steps + pre_count
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

    if memo is None:
        memo = {}

    key = tuple(state)
    # if key in memo:
    #     return memo[key]

    path_set = set(tuple(inner_list) for inner_list in path)
    if len(path_set) != len(path):
        return (100000, None)

    if target == state:
        return (0, path.copy())

    # prevent infinite loop
    if depth > 10:
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
    initial_state: list[int],
    actions: list[list[int]],
):
    target = [0 for i in range(len(initial_state))]
    queue = deque([(initial_state, 0)])  # ([0,0,0,0], count)
    visited = set()

    while queue:
        joltage_state, count = queue.popleft()

        # If we reach the target amount, return the number of steps used
        if joltage_state == target:
            return (count, [])

        # Explore the next amounts we can make from current_amount using the coins
        for action in actions:
            _, new_joltage = perform_action(joltage_state, action, joltage_state)
            if all(n >= 0 for n in joltage_state):
                if tuple(new_joltage) not in visited:
                    visited.add(tuple(new_joltage))
                    queue.append((new_joltage, count + 1))
            else:
                print(f"skip. {len(queue)}, {joltage_state}")

    return (-1, [])


def coin_change_bfs(coins, target):
    # Initialize a queue for BFS and a visited set to keep track of visited amounts
    queue = deque([(0, 0)])  # (current_amount, number_of_coins)
    visited = set()

    while queue:
        current_amount, num_coins = queue.popleft()

        # If we reach the target amount, return the number of coins used
        if current_amount == target:
            return num_coins

        # Explore the next amounts we can make from current_amount using the coins
        for coin in coins:
            next_amount = current_amount + coin

            # Only consider the next amount if it is less than or equal to the target
            # and has not been visited before
            if next_amount <= target and next_amount not in visited:
                visited.add(next_amount)  # Mark this amount as visited
                queue.append(
                    (next_amount, num_coins + 1)
                )  # Add next amount to the queue with incremented coin count

    # If we exhaust the queue without finding the target, return -1
    return -1


def perform_action(
    state: list[bool], action_arr: list[int], joltage_input: list[int] = None
) -> tuple[list[bool], list[int]]:
    # Create a copy to avoid mutating the original state
    new_state = state.copy()
    joltages = joltage_input.copy() if joltage_input else None

    for action in action_arr:
        new_state[action] = not new_state[action]
        if joltage_input:
            joltages[action] -= 1

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
    # Example usage
    # coins = [2, 11]
    # target = 55
    # result = coin_change_bfs(coins, target)
    # print(result)  # Output should be 3 (11 can be made with two 5s and one 1)
