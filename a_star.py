import puzzle.puzzle as problem_p
import robot.robot as problem_b
import copy
import sys
from heapq import *
def a_star():

    if len(sys.argv) != 2:
        print ("Usage:\n python a_star.py [puzzle/robot]")
        sys.exit(0)

    problem = None
    if sys.argv[1] == 'puzzle':
        problem = problem_p
    elif sys.argv[1] == 'robot':
        problem = problem_b
    else:
        sys.exit(0)




    cur = problem.initialize()
     
    to_expand = []
    expanded = []
    heapify(to_expand)
    while True:

#        print (str(cur.paid) + "   " + str(cur.heuristic) + "   " + str(cur.full_paid()))
        

        actions = problem.actions(cur)
        expanded.append(cur)

        if problem.goal(cur):
            print("problem solved!!")
            print_path_cost(cur,len(expanded), len(expanded), len(expanded) + len(to_expand), problem)
            break
        
        for action in actions:
            state = problem.result(copy.deepcopy(cur), action)
            if not_contains(state, expanded, to_expand):
                state.path = cur.path + [{'state': cur, 'action': action}]
                heappush(to_expand, state)
                state.heuristic = problem.heuristic(state) 
                state.paid = cur.paid + problem.cost_step(cur, action)
        
        if len(to_expand) == 0:
            print("no answer!!!")
            break

        cur = heappop(to_expand)
        
        
    
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
