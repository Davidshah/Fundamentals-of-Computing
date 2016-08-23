# Project 1 for Algorithmic Thinking class, By DJS, 09/16/2015
# Degree distributions for graphs

'''
Three example graphs assigned in project 1
'''

EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 4, 5, 6, 7, 3])}

def make_complete_graph(num_nodes):
    '''
    Takes the number of nodes num_nodes and returns a
    dictionary corresponding to a complete directed graph
    with the specified number of nodes.
    '''
    complete_graph = {}
    set_nodes = set(range(num_nodes))
    
    for node in range(num_nodes):
        # all nodes except for self-loops (not allowed)
        complete_graph[node] = set_nodes.difference(set([node]))

    return complete_graph

    
def compute_in_degrees(digraph):
    '''
    Takes a directed graph digraph (represented as a dictionary)
    and computes the in-degrees for the nodes in the graph.
    '''
    in_degrees = {}
    list_nodes = []
    
    for node in digraph:
        # need to convert set to list
        list_nodes.extend(list(digraph[node]))

    for node in digraph:
        # count occurances of each degree
        in_degrees[node] = list_nodes.count(node)

    return in_degrees    
    
    
def in_degree_distribution(digraph):
    '''
    Takes a directed graph digraph (represented as a dictionary)
    and computes the unnormalized distribution of the in-degrees of the graph.
    '''
    degree_distribution = {}
    list_indegrees = []
    in_degrees = compute_in_degrees(digraph)

    for degree in in_degrees:
        list_indegrees.append(in_degrees[degree])

    for degree in list_indegrees:
        if degree not in degree_distribution.keys():
            # first occurance, initialize to 1
            degree_distribution[degree] = 1
        else:
            # increment next occurance(s)
            degree_distribution[degree] += 1

    return degree_distribution     
    