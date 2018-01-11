#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 3: Reliable Communications

Team Number:
Student Names:
'''
import unittest
import sys
import math
import itertools
import heapq
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

class PriorityQueue:
    """Priority Queue

    An efficient priority queue implementation, as described in
    the heapq library of the python manual [1].

    [1]: http://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes
    """
    def __init__(self):
        self.pqueue = []                  # list of entries arranged in a heap
        self.entry_finder = {}            # mapping of tasks to entries
        self.REMOVED = '<removed-task>'   # placeholder for a removed task
        self.counter = itertools.count()  # unique sequence count

    def add_task(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pqueue, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pqueue:
            priority, count, task = heapq.heappop(self.pqueue)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task

        raise KeyError('pop from an empty priority queue')

    """Auxiliary Functions"""
    def get_priority(self, task):
        """
        Sig: integer ==> integer
        Pre: task is a task that exists in entry_finder
        Post:
        Example: pq.get_priority(5)==>10
        """
        entry = self.entry_finder[task]
        return entry[0]

    def length(self):
        """
        Sig:  ==> integer
        Pre:
        Post:
        Example: pq.length()==>5
        """
        return len(self.entry_finder)


def reliable(G, s, t):
    """
    Sig: graph G(V,E), vertex, vertex ==> vertex[0..k]
    Pre:
    Post:
    Example: TestCase 1
    """

    tovisit = PriorityQueue()
    pred = {}
    dist = {}
    pi = {}
    path = []

    #Perform Dijkstra's Algorithm
    for node in G.nodes():
        # Variant: len(G.nodes())-G.nodes().index(node)
        pred[node] = None
        if node != s:
            pi[node] = 1000000
            tovisit.add_task(node, pi[node])

    pi[s] = 0
    tovisit.add_task(s, pi[s])

    while tovisit.length()!=0:
        # Variant: tovisit.length()
        node = tovisit.pop_task()
        for neighbor in G.neighbors(node):
            #Avoid log(0)
            if G[node][neighbor]['fp']<1:
                l = pi[node] - math.log(1-G[node][neighbor]['fp'])
            elif G[node][neighbor]['fp']==1:
                l = 0
            if pi[neighbor] > l:
                tovisit.add_task(neighbor, l)
                pi[neighbor] = l
                pred[neighbor]=node

    #Reconstruct path
    node = t
    while node!=s:
        # Variant: len(G.edges())-len(path)
        path.insert(0, node)
        node = pred[node]
    path.insert(0, node)

    return path


class ReliableCommunicationsTest(unittest.TestCase):
    """Test suite for the reliable communications problem
    """
    def draw_mst(self, G, path, n):
        if not HAVE_PLT:
            return
        pos = nx.spring_layout(G) # positions for all nodes
        plt.subplot(120 + n)
        plt.title('Reliability %d' % n)
        plt.axis('off')
        # nodes
        nx.draw_networkx_nodes(G, pos, node_size = 700)
        # edges
        nx.draw_networkx_edges(G, pos, width = 6, alpha = 0.5,
                               edge_color = 'b', style = 'dashed')
        from itertools import izip
        l = [(a, b) for a, b in izip(path[0:-1], path[1:])]
        T = nx.Graph()
        T.add_edges_from(l)
        nx.draw_networkx_edges(T, pos, width = 6)
        # labels
        nx.draw_networkx_labels(G, pos, font_size = 20, font_family = 'sans-serif')
    def test_sanity1(self):
        G = nx.Graph()
        G.add_edge('a', 'b', fp = 0.6)
        G.add_edge('a', 'c', fp = 0.2)
        G.add_edge('c', 'd', fp = 0.1)
        G.add_edge('c', 'e', fp = 0.7)
        G.add_edge('c', 'f', fp = 0.9)
        G.add_edge('a', 'd', fp = 0.3)
        path = reliable(G, 'b', 'f')
        self.assertEqual(path, ['b', 'a', 'c', 'f'], 'test 1 failed')
        #self.draw_mst(G, path, 1)

    def test_sanity2(self):
        G = nx.Graph()
        G.add_edge('a', 'b', fp = 0.6)
        G.add_edge('a', 'c', fp = 0.9)
        G.add_edge('c', 'd', fp = 0.1)
        G.add_edge('c', 'e', fp = 0.7)
        G.add_edge('c', 'f', fp = 0.9)
        G.add_edge('a', 'd', fp = 0.3)
        path = reliable(G, 'b', 'f')
        self.assertEqual(path, ['b', 'a', 'd', 'c', 'f'], 'test 2 failed')
        #self.draw_mst(G, path, 2)
    @classmethod
    def tearDownClass(cls):
        if HAVE_PLT:
            plt.show() # display

if __name__ == '__main__':
    unittest.main()
