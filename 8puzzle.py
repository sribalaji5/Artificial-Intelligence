import heapq

moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            distance += abs(i // 3 - (state[i] - 1) // 3) + abs(i % 3 - (state[i] - 1) % 3)
    return distance

def solve_puzzle(initial_state, goal_state):
    open_list = [(heuristic(initial_state), initial_state, [])]
    closed_set = set()

    while open_list:
        _, current_state, steps = heapq.heappop(open_list)

        if current_state == goal_state:
            return steps + [current_state]

        closed_set.add(current_state)
        blank_index = current_state.index(0)

        for move in moves[blank_index]:
            new_state = list(current_state)
            new_state[blank_index], new_state[move] = new_state[move], new_state[blank_index]
            new_state_tuple = tuple(new_state)

            if new_state_tuple not in closed_set:
                new_steps = steps + [current_state]
                heapq.heappush(open_list, (heuristic(new_state), new_state_tuple, new_steps))

    return None

def print_puzzle_steps(solution_steps):
    for step_num, step in enumerate(solution_steps):
        print(f"\nStep {step_num + 1}:")
        for i in range(0, 9, 3):
            print(step[i:i + 3])

initial_state = tuple(map(int, input("Enter the initial state of the puzzle (use 0 for the blank space): ").split()))
goal_state = tuple(map(int, input("Enter the goal state of the puzzle: ").split()))

print("\nInitial State:")
print_puzzle_steps([initial_state])

solution_steps = solve_puzzle(initial_state, goal_state)

if solution_steps:
    print("\nSolution steps:")
    print_puzzle_steps(solution_steps)
else:
    print("No solution found.")
