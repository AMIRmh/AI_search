class state:
    def __init__(self):
        self.path = []
        self.val = [[] for i in range(3)]
        self.heuristic = 0
        self.paid = 0

    def full_paid(self):
        return self.heuristic + self.paid

    def __lt__(self, other):
        return self.full_paid() < other.full_paid()

    def __eq__(self, other):
        return self.val == other.val



def initialize():
    arr = [[] for i in range(3)]
    with open("puzzle/input_puzzle", "r") as f:
        i = 0
        for line in f:
            line = line.replace(' ', '').replace('\n', '')
            arr[i].extend(line)
            i = i + 1
    
    init_state = state()
    init_state.val = arr
    init_state.heuristic = heuristic(init_state)
    return init_state


def actions(state):
    actions = []
    for i in range(3):
        for j in range(3):
            if state.val[i][j] == '0':
                if j == 0:
                    actions.append('R')
                elif j == 2:
                    actions.append('L')
                else:
                    actions.extend('LR')

                if i == 0:
                    actions.append('D')
                elif i == 2:
                    actions.append('U')
                else:
                    actions.extend('DU')
                
                return actions


def goal(state):
    goal = [['0','1','2'],['3','4','5'],['6','7','8']]

    if state.val == goal:
        return True
    return False


def result(state, action):
    for i in range(3):
        for j in range(3):
            if state.val[i][j] == '0':
                if action == 'U':
                    state.val[i-1][j], state.val[i][j] = state.val[i][j], state.val[i-1][j]
                elif action == 'R':
                    state.val[i][j+1], state.val[i][j] = state.val[i][j], state.val[i][j+1]
                elif action == 'D':
                    state.val[i+1][j], state.val[i][j] = state.val[i][j], state.val[i+1][j]
                elif action == 'L':
                    state.val[i][j-1], state.val[i][j] = state.val[i][j], state.val[i][j-1]

                return state

def cost_step(state, action):
    return 1


def heuristic(state):
    goal = {'0':(0,0),
            '1':(0,1),
            '2':(0,2),
            '3':(1,0),
            '4':(1,1),
            '5':(1,2),
            '6':(2,0),
            '7':(2,1),
            '8':(2,2)
            }
    
    cost = 0
    for i in range(3):
        for j in range(3):
            if state.val[i][j] != '0':
                cost = cost + abs(goal.get(state.val[i][j])[0] - i) + abs(goal.get(state.val[i][j])[1] - j)
    return cost
