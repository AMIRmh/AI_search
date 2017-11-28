import puzzle.puzzle as problem_p
import copy
import sys

def a_star():
    problem = None
    if sys.argv[1] == 'puzzle':
        problem = problem_p
    else:
        sys.exit(0)




    cur = problem.initialize()
     
    to_expand = []
    expanded = []
    second_best = problem.state()
    second_best.heuristic = 100000000
    second_best.paid = 100000000
    while True:

        print (str(cur.paid) + "   " + str(cur.heuristic) + "   " + str(cur.full_paid()))
        

        actions = problem.actions(cur)
        expanded.append(cur)
        currently_expanded = []

        if problem.goal(cur):
            print("problem solved!!")
            print_path_cost(cur,len(expanded), len(expanded), len(expanded) + len(to_expand), problem)
            break
        
        selected = second_best
        for action in actions:
            state = problem.result(copy.deepcopy(cur), action)
            if not_contains(state, expanded, to_expand):
                state.path = cur.path + [{'state': cur, 'action': action}]
                currently_expanded.append(state)
                state.heuristic = problem.heuristic(state) 
                state.paid = cur.paid + problem.cost_step(cur, action)

                if state.full_paid() < selected.full_paid():
                    selected = state
        
        
        if (len(to_expand) == 0) and (len(currently_expanded) == 0):
            print("no answer!!!")
            break
        
        
        cur = selected
        if selected == second_best:
            to_expand.remove(cur)
            to_expand.extend(currently_expanded)
            selected = to_expand[0]
            for state in currently_expanded:
                if selected.full_paid() > state.full_paid():
                    selected = state
            second_best = selected
        else:
            currently_expanded.remove(cur)
            to_expand.extend(currently_expanded)
            selected = second_best
            for state in currently_expanded:
                if state.full_paid() < selected.full_paid():
                    selected = state
            second_best = selected

def not_contains(state, expanded, to_expand):
    for f in to_expand:
        if state.val == f.val:
            if state.full_paid() < f.full_paid():
                f.path = state.path
            return False

    for e in expanded:
        if state.val == e.val:
            return False

    return True


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



a_star()
