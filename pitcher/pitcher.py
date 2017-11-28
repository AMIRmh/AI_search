class state:
    def __init__(self, val1, val2):
        self.path = []
        self.val = [val1,val2] # self.val[0] = 3 litre and self.val[1] = 4 litre
        self.heuristic = 0
        self.paid = 0


    def full_paid(self):
        return self.heuristic + self.paid



def initialize():
    return state(0,0)

def initialize_goal():
    return [state(0,2), state(1,2), state(2,2), state(3,2)]


# e -> empty 
# f -> fill
# t -> to
def actions(state):
    actions = []
    if state.val[0] != 0:
        actions.append('1e')
        if state.val[1] < 4:
            actions.append('1t2')
    else:
        actions.append('1f')


    if state.val[1] != 0:
        actions.append('2e')
        if state.val[0] < 3:
            actions.append('2t1')
    else:
        actions.append('2f')

    return actions



def goal(state):
    if state.val[1] == 2:
        return True
    return False


def result(state, action):
    if action == '1e':
        state.val[0] = 0
    elif action == '2e':
        state.val[1] = 0
    elif action == '1f':
        state.val[0] = 3
    elif action == '2f':
        state.val[1] = 4
    elif action == '1t2':
        if state.val[0] + state.val[1] > 4:
            state.val[0] = state.val[0] - (4 - state.val[1])
            state.val[1] = 4
        else:
            state.val[1] = state.val[1] + state.val[0]
            state.val[0] = 0
    elif action == '2t1':
        if state.val[0] + state.val[1] >= 3:
            state.val[1] = state.val[1] - (3 - state.val[0])
            state.val[0] = 3
        else:
            state.val[0] = state.val[1] + state.val[0]
            state.val[1] = 0

    return state


def cost_step(state, action):
    return 1


def actions_rev(state):
    actions = []
    if state.val[0] == 0:
        actions.append('1e')
        if state.val[1] != 0:
            actions.append('1t2')
    elif state.val[0] == 3:
        actions.append('1f')
        if state.val[1] != 4:
            actions.append('2t1')
    else:
        if state.val[1] == 0:
            actions.append('2t1')
        elif state.val[1] == 4:
            actions.append('1t2')


    if state.val[1] == 0:
        actions.append('2e')
        if state.val[0] != 0:
            actions.append('2t1')
    elif state.val[1] == 4:
        actions.append('2f')
        if state.val[0] != 3:
            actions.append('1t2')
    else:
        if state.val[0] == 0:
            actions.append('1t2')
        elif state.val[0] == 3:
            actions.append('2t1')

    return list(set(actions))


def result_rev(s, action):
    val2 = s.val[1]
    val1 = s.val[0]

    if action == '1e':
        return [state(1,val2), state(2,val2), state(3,val2)]
    elif action == '2e':
        return [state(val1,1), state(val1,2), state(val1,3), state(val1,4)]
    elif action == '1f':
        return [state(0,val2), state(1,val2), state(2,val2), state(3,val2)]
    elif action == '2f':
        return [state(val1,0), state(val1,1), state(val1,2), state(val1,3), state(val1,4)]
    elif action == '1t2':
        new_states = []
        while True:
            val2 -= 1
            val1 += 1
            new_states.append(state(val1,val2))
            if val1 == 3 or val2 == 0:
                break
        return new_states
    elif action == '2t1':
        new_states = []
        while True:
            val1 -= 1
            val2 += 1
            new_states.append(state(val1,val2))
            if val2 == 4 or val1 == 0:
                break
        return new_states
