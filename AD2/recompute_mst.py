#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 2: Recomputing the minimum spanning tree

Team Number:
Student Names:
'''
import unittest
import networkx as nx
"""IMPORTANT:
We're using networkx only to provide a reliable graph
object.  Your solution may NOT rely on the networkx implementation of
any graph algorithms.  You can use the node/edge creation functions to
create test data, and you can access node lists, edge lists, adjacency
lists, etc. DO NOT turn in a solution that uses a networkx
implementation of a graph traversal algorithm, as doing so will result
in a score of 0.
"""
try:
    import matplotlib.pyplot as plt
    have_plt = True
except:
    have_plt = False

def ring_extended(G):
    """
    Sig: graph G(node,edge) ==> boolean, int[0..j-1]
    Pre:
    Post:
    Example:
        ring(g1) ==> False, []
        ring(g2) ==>  True, [3,7,8,6,3]
    """
    ringfound = False

    #If a ring is found, head represents the root node and its parent
    #(node, parent)
    head = (None,None)

    #Nodes to start the DFS from.
    startnodes = set(G.nodes())

    allvisited = set([])

    while len(allvisited)!=len(G.nodes()):
        # Variant: len(G.nodes()) - len(allvisited)
        startnode = startnodes.pop()

        #If start node is not connected to any other nodes, go to next iteration.
        if len(G.neighbors(startnode))==0:
            allvisited.add(startnode)
            continue

        #Reset visited and tovisit
        visited= {}
        tovisit=[(startnode,startnode)]

        while len(tovisit)!=0:
            # Variant: len(tovisit)
            node = tovisit.pop()
            #-1 is set as default value for visited.get(), i.e. visited.get(node)==-1
            #means node was not found in visited
            if (visited.get(node[0], -1)==-1) or (visited.get(node[1], -1)==-1):
                visited[node[0]] = node[1]
                allvisited.add(node[0])
                #Remove nodes that have been visited from startnodes since performing dfs
                #on them would be redundant
                startnodes.discard(node[0])
                for neighbor in G.neighbors(node[0]):
                    # Variant: len(G.neighbors(node[0])) - G.neighbors(node[0]).index(neighbor)
                    if neighbor!=node[1] and (visited.get(neighbor, -1)!=-1):
                        ringfound = True
                        head = (neighbor,node[0])
                        #Break outer loop
                        tovisit = []
                        #Break inner loop
                        break
                    if visited.get(neighbor, -1)==-1:
                        tovisit.append((neighbor,node[0]))
        #Break loop if ring has been found
        if ringfound:
            break

    #Obtain list of nodes in ring if one was found
    ring = []
    if ringfound:
        ring.extend(head)
        node = ring[-1]
        while node!=head[0]:
            # Variant: len(visited)-len(ring)
            ring.append(visited[node])
            node = ring[-1]

    return ringfound, ring

def update_MST_1(G, T, e, w):
    """
    Sig: graph G(V,E), graph T(V, E), edge e, int ==>
    Pre:
    Post:
    Example: TestCase 1
    """
    (u, v) = e
    assert(e in G.edges() and e not in T.edges() and w > G[u][v]['weight'])


def update_MST_2(G, T, e, w):
    """
    Sig: graph G(V,E), graph T(V, E), edge e, int ==>
    Pre:
    Post: Edge e in graph G with updated weight w,
          T updated to a new minimum spanning tree of updated G
    Example: TestCase 2
    """
    (u, v) = e

    #Update weight of edge (u,v) in G to w
    G[u][v]['weight'] = w
    #Add the same edge to T
    T.add_edge(u,v,weight=w)

    #Retrieve the new cycle using ring_extended
    isring, ring = ring_extended(T)

    #Dictionary used to get edge in cycle of T with highest value
    edgeweights = {}

    #Construct edgeweights
    for i in range(1,len(ring)):
        # Variant: len(ring)-i
        (u,v)=(ring[i],ring[i-1])
        edgeweights[(u,v)] = T.get_edge_data(u,v)['weight']

    #Find edge in cycle of T with highest weight and remove it from T
    e = max(edgeweights,key=edgeweights.get)
    T.remove_edge(e[0],e[1])

def update_MST_3(G, T, e, w):
    """
    Sig: graph G(V,E), graph T(V, E), edge e, int ==>
    Pre:
    Post:
    Example: TestCase 3
    """
    (u, v) = e
    assert(e in G.edges() and e in T.edges() and w < G[u][v]['weight'])


def update_MST_4(G, T, e, w):
    """
    Sig: graph G(V,E), graph T(V, E), edge e, int ==>
    Pre:
    Post:
    Example: TestCase 4
    """
    (u, v) = e
    assert(e in G.edges() and e in T.edges() and w > G[u][v]['weight'])

if __name__ == '__main__':
    unittest.main()
