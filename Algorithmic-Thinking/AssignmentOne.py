# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:50:48 2015

@author: David Shahrestani
"""

import urllib.request
import matplotlib.pyplot as pyplot
import matplotlib.pylab as pylab
import random

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib.request.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split(b'\n')
    graph_lines = graph_lines[ : -1]
    
    print("Loaded graph with", len(graph_lines), "nodes")
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(b" ")
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


def make_complete_graph(num_nodes):
    '''
    Takes the number of nodes num_nodes and returns a
    dictionary corresponding to a complete directed graph
    with the specified number of nodes.
    '''
    complete_graph = {}
    if num_nodes > 1:
        for node_no in range(0, num_nodes):
            complete_graph[node_no] = set([num for num in range(0, num_nodes) if num!=node_no])
    elif num_nodes == 1:
        complete_graph[0] = set([])
    return complete_graph;

    
def compute_in_degrees(digraph):
    """Computes indegrees of a digraph.
    """
    result = {}
    for key in digraph.keys():
        result[key] = 0
    for vset in digraph.values():
        for val in vset:
            result[val] += 1
    return result
    
    
def in_degree_distribution(digraph):
    """Computes indegree distribution of a digraph.
    """
    indeg = compute_in_degrees(digraph)
    result = {}
    sum_indegrees = 0
    for val in indeg.values():
        if val not in result:
            result[val] = 0
        result[val] += 1
    return result


def in_degree_norm_distribution(digraph):
    """Computes indegree distribution of a digraph.
    """
    indeg = compute_in_degrees(digraph)
    result = {}
    sum_indegrees = 0
    for val in indeg.values():
        if val not in result:
            result[val] = 0
        result[val] += 1
        sum_indegrees += 1
    for val in result.keys():
        result[val] = result[val] / float(sum_indegrees)
    return result
    
    
def generate_er_directed_graph(num_nodes, prob): 
    """ FOR QUESTION 2 """
    random_digraph = {}
    for nodex in range(0,num_nodes):
        for nodey in range(0,num_nodes):
            if nodey != nodex:
                rand = random.random()
                if nodex not in random_digraph:
                    random_digraph[nodex] = set([])
                if (rand < prob):
                    random_digraph[nodex].add(nodey)
    return random_digraph
    
    
def calculate_out_degrees(digraph):
    """ FOR QUESTION 3: COMPUTES THE UNNORMALIZED DISTRIBUTION OF THE OUT-DEGREES OF A GIVEN GRAPH (REPRESENTED AS ADJACENCY LIST """
    out_degrees_dict = {}
    if len(digraph) > 0:
        for from_node, to_nodes in digraph.items():
            if from_node in out_degrees_dict:
                out_degrees_dict[from_node] += len(to_nodes)
            else:
                out_degrees_dict[from_node] = len(to_nodes)
    return out_degrees_dict
    
    
def calculate_average_value(values_dict):
    """ FOR QUESTION 3: COMPUTES THE UNNORMALIZED DISTRIBUTION OF THE OUT-DEGREES OF A GIVEN GRAPH (REPRESENTED AS ADJACENCY LIST """
    values_total = 0.0
    avg_val = 0
    if len(values_dict) > 0:
        # value IS A NO. OF NODES HAVING AN OUT-DEGREE = NODE 
        for node, value in values_dict.items():
            values_total += value
        avg_val = int(values_total/len(values_dict))
    return avg_val
    

def generate_dpa_graph(tot_num_nodes,min_nodes):
    """ FOR QUESTION 4 : Algorithm DPA"""
#     DPATrial CLASS USAGE
#     SELECT A RANDOM NODE FROM THOSE IN THE DPA OBJECT
#     random.choice(dpa_object._node_numbers)
#     GET NO. OF NODES IN THE DPA OBJECT (INCL. DUPLICATES THAT REPRESENT INCREASED PROBABILITY OF SELECTION OF THOSE NODES)
#     dpa_object._num_nodes
#     LOOP count TIMES AND CHOOSE A NODE NUMBER AT RANDOM IN EACH LOOP AND ADD IT TO A SET THAT WILL FORM THE NEW EDGES  
#     dpa_object.run_trial(count)

    dpa_graph = make_complete_graph(min_nodes)
    dpa_object = DPATrial(min_nodes+1);
   
    for new_node in range(min_nodes, tot_num_nodes):
        dpa_graph[new_node] = set([])
        dpa_object.run_trial(min_nodes+1)
        for edge_to in range(0,min_nodes+1):
            dpa_graph[new_node].add(random.choice(dpa_object._node_numbers))
    return dpa_graph;

citation_graph = load_graph(CITATION_URL)
dpa_graph = generate_dpa_graph(27770,12)
dpa_distribution = in_degree_norm_distribution(dpa_graph)
citation_distribution = in_degree_norm_distribution(citation_graph)

pylab.rcParams['figure.figsize'] = 16, 12

pyplot.xscale('log')
pyplot.yscale('log')
pyplot.xlabel('in-degree')
pyplot.ylabel('share of nodes')
pyplot.title('DPA random graph vs. citation graph in-degree normalized distribution')
pyplot.plot([x for (x, y) in dpa_distribution.items()], [y for (x, y) in dpa_distribution.items()], 'r.', label='DPA')
pyplot.plot([x for (x, y) in citation_distribution.items()], [y for (x, y) in citation_distribution.items()], 'g.', label='Citation')
pyplot.legend()

pyplot.show()



