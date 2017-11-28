import puzzle.puzzle as problem_p
import pitcher.pitcher as problem_pt
import copy
import sys

def dfs():

    if len(sys.argv) != 4:
        print('Usage:\n python dfs.py [pitcher,puzzle] [depth] [graph/tree]')
        sys.exit(0)

    problem = None
    if sys.argv[1] == 'puzzle':
        problem = problem_p
    elif sys.argv[1] == 'pitcher':
        problem = problem_pt
    else:
        sys.exit(0)




    cur = problem.initialize()
    
    to_expand = []
    expanded = []
    
    while True:

        actions = problem.actions(cur)
        expanded.append(cur)
        
        if problem.goal(cur):
            print("problem solved!!")
            print_path_cost(cur,len(expanded), len(expanded), len(expanded) + len(to_expand), problem)
            break
        
        if len(cur.path) <= int(sys.argv[2]):
            for action in actions:
                state = problem.result(copy.deepcopy(cur), action)
                if not_contains(state, expanded, to_expand):
                    state.path = cur.path + [{'state': cur, 'action': action}]
                    to_expand.append(state)
                
            
        if len(to_expand) == 0:
            print("no answer!!!")
            break
        
        
        cur = to_expand.pop(-1)


def not_contains(state, expanded, to_expand):
    for f in to_expand:
        if state.val == f.val:
            return False
    
    if sys.argv[3] == 'graph':
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



dfs()
    

	
	

