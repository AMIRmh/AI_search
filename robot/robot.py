class state:
    robot_map = None
    row = None
    column = None
    def __init__(self, val1, val2):
        self.path = []
        self.val = [val1, val2]
        self.heuristic = 0
        self.paid = 0

    def full_paid(self):
        return self.heuristic + self.paid

    def __lt__(self, other):
        return self.full_paid() < other.full_paid()

    def __eq__(self, other):
        return self.val == other.val



def initialize():
    arr = None
    with open("robot/input_robot", "r") as f:
        i = 0
        for line in f:
            if i != 0:
                line = line.replace(' ', '').replace('\n', '')
                arr[i-1].extend(line)
            else:
                temp = list(line)
                state.row = int(temp[0])
                state.column = int(temp[1])
                arr = [[] for j in range(int(temp[0]))]
            i = i + 1

    state.robot_map = arr
    init_state = state(state.row - 1, 0)
    init_state.heuristic = heuristic(init_state)
    return init_state

def initialize_goal():
    goal = state(0, state.column - 1)
    return [goal]


def actions(state):
    actions = []
    if state.val[0] != 0 and state.robot_map[state.val[0] - 1][state.val[1]] != '0':
        actions.append('U')

    if state.val[0] != state.row - 1 and state.robot_map[state.val[0] + 1][state.val[1]] != '0':
        actions.append('D')

    if state.val[1] != 0 and state.robot_map[state.val[0]][state.val[1] - 1] != '0':
        actions.append('L')

    if state.val[1] != state.column - 1 and state.robot_map[state.val[0]][state.val[1] + 1] != '0':
        actions.append('R')

    return actions


def goal(state):
    return (state.val[0] == 0) and (state.val[1] == state.column - 1)

def result(state, action):
    if action == 'L':
        state.val[1] -= 1
        return state
    elif action == 'R':
        state.val[1] += 1
        return state
    elif action == 'U':
        state.val[0] -= 1
        return state
    elif action == 'D':
        state.val[0] += 1
        return state


def actions_rev(state):
    actions = []
    if state.val[0] != 0 and state.robot_map[state.val[0] - 1][state.val[1]] != '0':
        actions.append('D')

    if state.val[0] != state.row - 1 and state.robot_map[state.val[0] + 1][state.val[1]] != '0':
        actions.append('U')

    if state.val[1] != 0 and state.robot_map[state.val[0]][state.val[1] - 1] != '0':
        actions.append('R')

    if state.val[1] != state.column - 1 and state.robot_map[state.val[0]][state.val[1] + 1] != '0':
        actions.append('L')

    return actions

def result_rev(state, action):
    if action == 'D':
        state.val[0] -= 1
    elif action == 'U':
        state.val[0] += 1
    elif action == 'R':
        state.val[1] -= 1
    elif action == 'L':
        state.val[1] += 1
    return [state]
    

def cost_step(state, action):
    return 1


def heuristic(state):
    return (state.val[0]) + (state.column - state.val[1] - 1)
