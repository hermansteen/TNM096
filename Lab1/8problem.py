import copy
import time
import heapq

# define the initial state
#initialState = [1, 5, 2, 4, 0, 6, 7, 3, 8]
#initialState = [4, 1, 5, 7, 8, 2, 6, 3, 0]
#initialState = [0, 3, 4, 1, 6, 8, 7, 5, 2]
#initialState = [6, 4, 7, 8, 5, 0, 3, 2, 1]
initialState = [8, 6, 7, 2, 5, 4, 3, 0, 1]

# define the goal state
goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# define the actions
actions = ['up', 'down', 'left', 'right']

# node class for astar search tree


class Node:
    def __init__(self, state, parent, action, heuristic, cost=0, f=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = heuristic
        self.cost = cost
        self.f = f

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        # make string of state
        stateString = ""
        for i in range(len(self.state)):
            stateString += str(self.state[i])
        return hash(stateString)

    def expand(self):
        children = []
        for action in possible_actions(self.state):
            child = Node(None, self, action, None, self.cost+1, 0)
            child.state = execute(self.state, action)
            child.heuristic = heuristic1(child.state, goalState)
            child.f = child.heuristic + child.cost
            children.append(child)
        return children

    # print function for state, new line after 3 values
    def printState(self):
        for i in range(len(self.state)):
            for j in range(len(self.state[0])):
                print(self.state[i][j], end=" ")
                if (j == 2):
                    print("\n")

# define the function that returns the possible actions


def possible_actions(state):
    possible_actions = []
    for i in range(len(state)):
        if state[i] == 0:
            if i > 2:
                possible_actions.append('up')
            if i < 6:
                possible_actions.append('down')
            if i % 3 > 0:
                possible_actions.append('left')
            if i % 3 < 2:
                possible_actions.append('right')
    return possible_actions


def execute(state, action):
    tempState = state.copy()
    blankIndex = tempState.index(0)  # Find the index of the blank space

    if action == "left":
        # Swap the blank space with the element on the left
        tempState[blankIndex], tempState[blankIndex -
                                         1] = tempState[blankIndex - 1], tempState[blankIndex]
    elif action == "right":
        # Swap the blank space with the element on the right
        tempState[blankIndex], tempState[blankIndex +
                                         1] = tempState[blankIndex + 1], tempState[blankIndex]
    elif action == "up":
        # Swap the blank space with the element above
        tempState[blankIndex], tempState[blankIndex -
                                         3] = tempState[blankIndex - 3], tempState[blankIndex]
    elif action == "down":
        # Swap the blank space with the element below
        tempState[blankIndex], tempState[blankIndex +
                                         3] = tempState[blankIndex + 3], tempState[blankIndex]

    return tempState


def heuristic1(state, goal):
    n_errors = 0
    for i in range(len(state)):
        if state[i] != goal[i]:
            n_errors += 1
    return n_errors

# def heuristic1(state, goal):
#   # Manhattan distance heuristic
#   n_errors = 0
#   for i in range(len(state)):
#       if state[i] != goal[i]:
#           # Convert the flat index to 2D coordinates for both state and goal
#           state_row, state_col = divmod(i, 3)
#           goal_row, goal_col = divmod(goal.index(state[i]), 3)
#           # Calculate the Manhattan distance between the current tile and its goal position
#           n_errors += abs(state_row - goal_row) + abs(state_col - goal_col)
#   return n_errors


def astar(initial_state, goal_state):
    # define first node
    start_node = Node(initialState, None, None, 0, 0, 0)
    # define open list as a priority queue
    openList = []
    heapq.heappush(openList, start_node)
    n_iterations = 0
    closedList = {}  # Use a dictionary for closedList with state as key
    while openList:
        n_iterations += 1
        #print("iteration: ", n_iterations)
        currentNode = heapq.heappop(openList)
        closedList[currentNode] = currentNode  # Add current node to closedList
        if currentNode.state == goal_state:
            print("solution found")
            print("number of iterations: ", n_iterations)
            return currentNode
        else:
            children = currentNode.expand()
            for child in children:
                pushed = False
                if child in closedList:
                    existing_node = closedList[child]
                    if child.f < existing_node.f:
                        del closedList[child]
                        heapq.heappush(openList, child)
                        pushed = True
                    elif child.f >= existing_node.f:
                        pushed = True
                if not pushed:
                    heapq.heappush(openList, child)
    print("no solution")
    return None


def main():
    print("initial state: ")
    for i in range(len(initialState)):
        print(initialState[i])
    print("goal state: ")
    for i in range(len(goalState)):
        print(goalState[i])

    timer = time.time()
    solution = astar(initialState, goalState)
    print("time: ", (time.time() - timer), "s")
    print("solution: ")
    print(solution.state)
    print("solution path: ")
    path = []
    depth = 0
    while solution.parent is not None:
        path.append(solution.action)
        solution = solution.parent
        depth += 1
    path.reverse()
    print(path)
    print("depth: ", depth)


main()
