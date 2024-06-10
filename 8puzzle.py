import heapq

class PuzzleNode:
    def __init__(self, puzzle_state, parent=None, move=None):
        self.puzzle_state = puzzle_state
        self.parent = parent
        self.move = move
        if parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 0

    def __lt__(self, other):
        return (self.depth + self.heuristic()) < (other.depth + other.heuristic())

    def __eq__(self, other):
        return self.puzzle_state == other.puzzle_state

    def __hash__(self):
        return hash(str(self.puzzle_state))

    def __str__(self):
        return str(self.puzzle_state)

    def __repr__(self):
        return str(self)

    def find_blank(self):
        for i, row in enumerate(self.puzzle_state):
            for j, cell in enumerate(row):
                if cell == 0:
                    return i, j

    def possible_moves(self):
        i, j = self.find_blank()
        moves = []
        if i > 0:
            moves.append((-1, 0))
        if i < 2:
            moves.append((1, 0))
        if j > 0:
            moves.append((0, -1))
        if j < 2:
            moves.append((0, 1))
        return moves

    def apply_move(self, move):
        i, j = self.find_blank()
        di, dj = move
        new_state = [row[:] for row in self.puzzle_state]
        new_state[i][j] = new_state[i + di][j + dj]
        new_state[i + di][j + dj] = 0
        return new_state

    def heuristic(self):
        # Manhattan distance heuristic
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.puzzle_state[i][j] != 0:
                    value = self.puzzle_state[i][j] - 1
                    distance += abs(i - (value // 3)) + abs(j - (value % 3))
        return distance

def solve_puzzle(initial_state):
    initial_node = PuzzleNode(initial_state)
    frontier = [initial_node]
    visited = set()

    while frontier:
        node = heapq.heappop(frontier)
        if node.puzzle_state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return node
        visited.add(node)
        for move in node.possible_moves():
            new_state = node.apply_move(move)
            new_node = PuzzleNode(new_state, parent=node, move=move)
            if new_node not in visited:
                heapq.heappush(frontier, new_node)

    return None

def print_solution(solution_node):
    if solution_node is None:
        print("No solution found.")
        return
    path = []
    while solution_node:
        path.append(solution_node.puzzle_state)
        solution_node = solution_node.parent
    path.reverse()
    print("Solution steps:")
    for state in path:
        print_state(state)

def print_state(state):
    for row in state:
        print(row)
    print()

# Example usage:
initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
solution_node = solve_puzzle(initial_state)
print_solution(solution_node)
