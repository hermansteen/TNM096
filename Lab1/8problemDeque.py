import copy
import time
from collections import deque

# define the initial state
#initialState = [[1, 5, 2],
#               [4, 0, 6],
#               [7, 3, 8]]
#initialState = [[4, 1, 5],
#                [7, 8, 2],
#                [6, 3, 0]]

#initialState = [[0, 3, 4],
#               [1, 6, 8],
#               [7, 5, 2]]

initialState = [[6, 4, 7],
               [8, 5, 0],
               [3, 2, 1]]
#initialState = [[8, 6, 7],
#               [2, 5, 4],
#               [3, 0, 1]]


# define the goal state
goalState = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0]]

# define the actions
actions = ['up', 'down', 'left', 'right']

# node class for astar search tree


class Node:
    def __init__(self, state, parent, action, heuristic, cost, f=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = heuristic
        self.cost = cost
        self.f = f

    def expand(self):
        children = []
        for action in possible_actions(self.state):
            child = Node(None, self, action, None, self.cost)
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
        for j in range(len(state[0])):
            if state[i][j] == 0:
                if i > 0:
                    possible_actions.append('up')
                if i < len(state) - 1:
                    possible_actions.append('down')
                if j > 0:
                    possible_actions.append('left')
                if j < len(state[0]) - 1:
                    possible_actions.append('right')

    return possible_actions


def execute(state, action):
    tempState = copy.deepcopy(state)
    if (action == "left"):
        # find the position of the blank space
        for i in range(len(tempState)):
            for j in range(len(tempState[0])):
                if tempState[i][j] == 0:
                    # swap the blank space with the element on the left
                    tempState[i][j], tempState[i][j -
                                                  1] = tempState[i][j-1], tempState[i][j]
                    return tempState
    elif (action == "right"):
        # find the position of the blank space
        for i in range(len(tempState)):
            for j in range(len(tempState[0])):
                if tempState[i][j] == 0:
                    # swap the blank space with the element on the right
                    tempState[i][j], tempState[i][j +
                                                  1] = tempState[i][j+1], tempState[i][j]
                    return tempState
    elif (action == "up"):
        # find the position of the blank space
        for i in range(len(tempState)):
            for j in range(len(tempState[0])):
                if tempState[i][j] == 0:
                    # swap the blank space with the element above
                    tempState[i][j], tempState[i -
                                               1][j] = tempState[i-1][j], tempState[i][j]
                    return tempState
    elif (action == "down"):
        # find the position of the blank space
        for i in range(len(tempState)):
            for j in range(len(tempState[0])):
                if tempState[i][j] == 0:
                    # swap the blank space with the element below
                    tempState[i][j], tempState[i +
                                               1][j] = tempState[i+1][j], tempState[i][j]
                    return tempState


def heuristic1(state, goal):
    n_errors = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != goal[i][j]:
                if state[i][j] != 0:
                    n_errors += 1
    return n_errors

def compStates(state1, state2):
    for i in range(len(state1)):
        for j in range(len(state1[0])):
            if state1[i][j] != state2[i][j]:
                return False
    return True

""" def heuristic1(state, goal):
    # manhattan distance heuristic
    n_errors = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != goal[i][j]:
                for k in range(len(goal)):
                    for l in range(len(goal[0])):
                        if state[i][j] == goal[k][l]:
                            n_errors += abs(i-k) + abs(j-l)
    return n_errors """

def astar(initial_state, goal_state):
    # define first node
    node = Node(initial_state, None, None, 0, 0)
    # define open list
    openList = deque()
    closedList = deque()

    n_iterations = 0
    openList.append(node)

    while (openList):
        n_iterations += 1
        #print("iteration: ", n_iterations)
        #print("open list: ", len(openList))
        #print("lowest f value: ", openList[0].f)
        openList = deque(sorted(openList, key=lambda x: x.f))
        currentNode = openList.popleft()
        # put("PRESS ENTER TO CONTINUE.")
        #print("current node: ", currentNode.printState())
        closedList.append(currentNode)
        if currentNode.state == goal_state:
            print("solution found, det trodde du inte va?")
            print("number of iterations: ", n_iterations)
            return currentNode
        else:
            children = currentNode.expand()
            for child in children:
                pushed = False
                for node in closedList:
                    if node.state == child.state:
                        if child.f < node.f:
                            closedList.remove(node)
                            openList.append(child)
                            pushed = True
                        elif child.f >= node.f:
                            pushed = True
                for node in openList:
                    if node.state == child.state:
                        if child.f < node.f:
                            openList.remove(node)
                            openList.append(child)
                            pushed = True
                        elif child.f >= node.f:
                            pushed = True
                if not pushed:
                    openList.append(child)
    print("no solution")
    return None

def main():
    print("initial state: ")
    for i in range(len(initialState)):
        print(initialState[i])
    print("goal state: ")
    for i in range(len(goalState)):
        print(goalState[i])

    solution = astar(initialState, goalState)
    print("solution: ")
    print(solution.state)
    depth = 0
    while(solution.parent != None):
        depth += 1
        solution = solution.parent
    print("depth: ", depth)

#start timer
timer = time.time()
main()
# display time in ms
print("time: ", (time.time() - timer) * 1000, "ms")