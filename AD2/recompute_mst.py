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
    startnodes = G.nodes()
    allvisited = set([])

    while len(allvisited)!=len(G.nodes()):
        # Variant: len(G.nodes()) - len(allvisited)

        #Remove nodes that have been visited from startnodes since performing dfs
        #on them would be redundant
        startnodes = [e for e in startnodes if e not in allvisited]
        startnode = startnodes[0]

        #If start node is not connected to any other nodes, go to next iteration.
        if len(G.neighbors(startnode))==0:
            allvisited.add(startnode)
            continue

        visited=[]
        tovisit=[(startnode,startnode)]

        while len(tovisit)!=0:
            # Variant: len(tovisit)
            node = tovisit.pop()
            if set(node) not in [set(n) for n in visited]:
                visited.append(node)
                for neighbor in G.neighbors(node[0]):
                    # Variant: len(G.neighbors(node[0])) - G.neighbors(node[0]).index(neighbor)
                    if neighbor!=node[1] and (neighbor,node[0]) in visited:
                        ringfound = True
                        head = (neighbor,node[0])
                        #Break outer loop
                        tovisit = []
                        #Break inner loop
                        break
                    if (neighbor,node[0]) not in visited:
                        tovisit.append((neighbor,node[0]))
        #Break loop if ring has been found
        if ringfound:
            break

        #Insert visited nodes using current startnode into allvisited
        allvisited.update(zip(*visited)[0])

    #Obtain list of nodes in ring if one was found
    ring = []
    if ringfound:
        v = zip(*visited)[0]
        i = len(visited)-1
        ring.append(visited[i][0])
        while visited[i][0]!=head[0]:
            # Variant: len(visited)-len(ring)
            ring.append(visited[i][1])
            i = v.index(visited[i][1])
        ring.append(head[1])

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


class RecomputeMstTest(unittest.TestCase):
    """Test Suite for minimum spanning tree problem

    Any method named "test_something" will be run when this file is
    executed. Use the sanity check as a template for adding your own
    test cases if you wish.
    (You may delete this class from your submitted solution.)
    """
    def create_graph(self):
        G = nx.Graph()
        G.add_edge('a', 'b', weight = 0.6)
        G.add_edge('a', 'c', weight = 0.2)
        G.add_edge('c', 'd', weight = 0.1)
        G.add_edge('c', 'e', weight = 0.7)
        G.add_edge('c', 'f', weight = 0.9)
        G.add_edge('a', 'd', weight = 0.3)
        return G

    def draw_mst(self, G, T, n):
        if not have_plt:
            return
        pos = nx.spring_layout(G) # positions for all nodes
        plt.subplot(220 + n)
        plt.title('updated MST %d' % n)
        plt.axis('off')
        # nodes
        nx.draw_networkx_nodes(G, pos, node_size = 700)
        # edges
        nx.draw_networkx_edges(G, pos, width = 6, alpha = 0.5,
                               edge_color = 'b', style = 'dashed')
        nx.draw_networkx_edges(T, pos, width = 6)
        # labels
        nx.draw_networkx_labels(G, pos, font_size = 20, font_family = 'sans-serif')

    def test_mst1(self):
        """Sanity Test

        This is a simple sanity check for your function;
        passing is not a guarantee of correctness.
        """
        # TestCase 1: e in G.edges() and not e in T.edges() and
        #             w > G[u][v]['weight']
        G = self.create_graph()
        T = nx.minimum_spanning_tree(G)
        update_MST_1(G, T, ('a', 'd'), 0.5)
        # self.draw_mst(G, T, 1)
        # self.assertItemsEqual(
        #     T.edges(),
        #     [('a', 'b'), ('a', 'c'), ('c', 'd'), ('c', 'e'), ('c', 'f')]
        #     )

    def test_mst2(self):
        # TestCase 2: e in G.edges() and not e in T.edges() and
        #             w < G[u][v]['weight']
        G = self.create_graph()
        T = nx.minimum_spanning_tree(G)
        update_MST_2(G, T, ('a', 'd'), 0.1)
        #self.draw_mst(G, T, 2)
        self.assertItemsEqual(
            T.edges(),
            [('a', 'b'), ('a', 'd'), ('c', 'd'), ('c', 'e'), ('c', 'f')]
            )

    def test_mst3(self):
        # TestCase 3: e in G.edges() and e in T.edges() and
        #             w < G[u][v]['weight']
        G = self.create_graph()
        T = nx.minimum_spanning_tree(G)
        update_MST_3(G, T, ('a', 'c'), 0.1)
        # self.draw_mst(G, T, 3)
        # self.assertItemsEqual(
        #     T.edges(),
        #     [('a', 'b'), ('a', 'c'), ('c', 'd'), ('c', 'e'), ('c', 'f')]
        #     )

    def test_mst4(self):
        # TestCase 4: e in G.edges() and e in T.edges() and
        #             w > G[u][v]['weight']
        G = self.create_graph()
        T = nx.minimum_spanning_tree(G)
        update_MST_4(G, T, ('a', 'c'), 0.4)
        #self.draw_mst(G, T, 4)
        # self.assertItemsEqual(
        #     T.edges(),
        #     [('a', 'b'), ('a', 'd'), ('c', 'd'), ('c', 'e'), ('c', 'f')]
        #     )

    @classmethod
    def tearDownClass(cls):
        if have_plt:
            plt.show()
if __name__ == '__main__':
    unittest.main()
