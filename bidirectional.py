import pitcher.pitcher as problem_pt
import robot.robot as problem_r
import sys
import copy

def bidirectional():

    if len(sys.argv) != 2:
        print ("Usage:\n python bidirectional.py [pitcher/robot]")
        sys.exit(0)

    problem = None
    if sys.argv[1] == 'pitcher':
        problem = problem_pt
    elif sys.argv[1] == 'robot':
        problem = problem_r
    else:
        sys.exit(0)
    
    
    cur = problem.initialize()

    to_expand_cur = []
    expanded_cur = []
    
    to_expand_goal = problem.initialize_goal()
    goal_state = to_expand_goal.pop(0)
    expanded_goal = []
    
    while True:

        actions = problem.actions(cur)
        expanded_cur.append(cur)
        found_state = not_contains(cur, to_expand_goal)
        if found_state != None:
            cur.path = cur.path + found_state.path
            print("problem solved!!")
            print_path_cost(cur, len(expanded_cur) + len(expanded_goal), len(expanded_cur) + len(expanded_goal), len(expanded_goal) + len(to_expand_goal) + len(to_expand_cur) + len(expanded_cur), problem)
            break
        
        for action in actions:
            state = problem.result(copy.deepcopy(cur), action)
            if not_contains(state, expanded_cur, to_expand_cur) is None:
                state.path = cur.path + [{'state': cur, 'action': action}]
                to_expand_cur.append(state)
                

######################################################## goal part

        actions = problem.actions_rev(goal_state)
        expanded_goal.append(goal_state)
        found_state = not_contains(goal_state, to_expand_cur)
        if found_state != None:
            cur.path = found_state.path + goal_state.path
            print("problem solved!!")
            print_path_cost(cur, len(expanded_cur) + len(expanded_goal), len(expanded_cur) + len(expanded_goal), len(expanded_goal) + len(to_expand_goal) + len(to_expand_cur) + len(expanded_cur), problem)
            break

        
        for action in actions:
            states = problem.result_rev(copy.deepcopy(goal_state), action)
            for state in states:
                if not_contains(state, expanded_goal, to_expand_goal) is None:
                    state.path = [{'state': goal_state, 'action': action}] +  goal_state.path
                    to_expand_goal.append(state)

        if len(to_expand_cur) == 0 and len(to_expand_goal) == 0:
            print("no answer!!!")
            break

        if len(to_expand_goal) != 0:
            goal_state = to_expand_goal.pop(0)
        
        if len(to_expand_cur) != 0:   
            cur = to_expand_cur.pop(0)


def not_contains(state, expanded, to_expand = None):
    if to_expand != None:
        for f in to_expand:
            if state.val == f.val:
                return f

    for e in expanded:
        if state.val == e.val:
            return e

    return None

#def not_contains(state, to_expand):
#    for f in to_expand:
#        if state.val == f.val:
#            return f
#    return None

def print_path_cost(node, seen_nodes, expanded_nodes, mem_used, problem):
    path = []
    cost = 0
    for path_info in node.path:
        path.append(path_info.get('action'))
        cost = cost + problem.cost_step(path_info.get('state'), path_info.get('action'))
    
    print("path: " + str(path))
    print("cost: " + str(cost))
    print("seen nodes: " + str(seen_nodes))
    print("expanded nodes: " + str(expanded_nodes))
    print("memory used: " + str(mem_used))

bidirectional()
