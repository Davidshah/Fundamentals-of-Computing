"""
Student template code for Project 3

"""

import math
import alg_cluster

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list
    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)
    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    result = (float("inf"), -1, -1)
    nnn = len(cluster_list)
    if nnn == 1:
        return result
    for idx1 in xrange(nnn - 1):
        for idx2 in xrange(idx1 + 1, nnn):
            current_d = pair_distance(cluster_list, idx1, idx2)
            if current_d < result:
                result = current_d
    return result



def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)
    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    num = len(cluster_list)
    if num <= 3:
        return slow_closest_pair(cluster_list)
    else:
        mid = int(math.floor(0.5 * num))
        p_l = [cluster_list[idx] for idx in xrange(mid)]
        p_r = [cluster_list[idx] for idx in xrange(mid, num)]
        result = fast_closest_pair(p_l)
        new_res   = fast_closest_pair(p_r)
        new_res = (new_res[0], new_res[1] + mid, new_res[2] + mid)
        if new_res < result:
            result = new_res
        mid = 0.5 * (p_l[-1].horiz_center() 
                     + p_r[0].horiz_center())
        new_res   = closest_pair_strip(cluster_list, 
                                    mid, result[0])
        if new_res < result:
            result = new_res
    return result


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """
    mid = [idx for idx in xrange(len(cluster_list)) 
           if abs(cluster_list[idx].horiz_center() 
                  - horiz_center) < half_width]
    mid.sort(key = lambda idx: cluster_list[idx].vert_center())
    num = len(mid)
    result = (float("inf"), -1, -1)
    for idx1 in xrange(num - 1):
        for idx2 in xrange(idx1 + 1, min(idx1 + 4, num)):
            current_d = pair_distance(cluster_list, mid[idx1], mid[idx2])
            if current_d < result:
                result = current_d
    if result[1] > result[2]:
        result = (result[0], result[2], result[1])
    return result

def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    num = len(cluster_list)
    while num > num_clusters:	
        cluster_list.sort(key = lambda clu: clu.horiz_center())
        idx = fast_closest_pair(cluster_list)
        cluster_list[idx[1]].merge_clusters(cluster_list[idx[2]])
        cluster_list.pop(idx[2])
        num -= 1
    return cluster_list
    
    
    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    
    Input: List of clusters, number of clusters, number of iterations
    Output: List of clusters whose length is num_clusters
    """
    cluster_list_sorted = sorted(cluster_list, key = lambda x: x.total_population(), reverse = True)
    k_clusters = cluster_list_sorted[:num_clusters]
    # initialize k-means clusters to be initial clusters with largest populations
    for dummy_idx in xrange(num_iterations):
        new_clusters = [alg_cluster.Cluster(set([]), 0, 0, 1, 0) for dummy_idx in xrange(num_clusters)]
        for idx_j in xrange(len(cluster_list)):
            current_dist = [cluster_list[idx_j].distance(k_clusters[idx_l]) for idx_l in xrange(num_clusters)]
            idx_l = min(xrange(len(current_dist)), key=current_dist.__getitem__)
            new_clusters[idx_l].merge_clusters(cluster_list[idx_j])      
        k_clusters = new_clusters[:]
            
    return k_clusters
