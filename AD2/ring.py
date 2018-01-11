#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 2: Ring Detection

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
    HAVE_PLT = True
except ImportError:
    HAVE_PLT = False

def ring(G):
    """
    Sig: graph G(node,edge) ==> boolean
    Pre:
    Post:
    Example:
        ring(g1) ==> False
        ring(g2) ==> True
    """
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
                        return True
                    if visited.get(neighbor, -1)==-1:
                        tovisit.append((neighbor,node[0]))
    return False


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

def draw_graph(G,r):
    """Draw graph and the detected ring
    """
    if not HAVE_PLT:
        return
    pos = nx.spring_layout(G)
    plt.axis('off')
    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_edges(G,pos,style='dotted') # graph edges drawn with dotted lines
    nx.draw_networkx_labels(G,pos)

    # add solid edges for the detected ring
    if len(r) > 0:
        T = nx.Graph()
        T.add_path(r)
        for (a,b) in T.edges():
            if G.has_edge(a,b):
                T.edge[a][b]['color']='g' # green edges appear in both ring and graph
            else:
                T.edge[a][b]['color']='r' # red edges are in the ring, but not in the graph
        nx.draw_networkx_edges(
            T,pos,
            edge_color=[edata['color'] for (a,b,edata) in T.edges(data=True)],
            width=4)
    plt.show()
