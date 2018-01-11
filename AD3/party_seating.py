#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 3: Party seating problem

Team Number:
Student Names:
'''
import unittest

# If your solution needs a queue, you can use this one:
from collections import deque

def party(known):
    """
    Sig:    int[1..m, 1..n] ==> boolean, int[1..j], int[1..k]
    Pre:
    Post:
    Ex:     [[1,2],[0,3],[0],[1]] ==> True, [0,3], [1,2]
    """

    #For this solution, a node denotes an index of input list known

    #Table A and B. Stores indices of known, aka guests/nodes.
    A = set()
    B = set()

    #Dict in which 0=not seated, 1=seated at table A, 2=seated at table B
    #Example: seated[2] = 2; Guest 2 seated at table B
    seated = {i:0 for i in range(len(known))}

    #Nodes to start DFS on. Initially all nodes
    startnodes = set([i for i in range(len(known))])

    #All nodes that have been visited
    allvisited = set()

    #Dict in which the parent node of any node X is stored.
    #Parent node denotes the node from which node X was discovered during DFS
    parent = {}

    while len(allvisited)!=len(known):
        # Variant: len(known)-len(allvisited)

        startnode = startnodes.pop()

        #Node not connected to any other node it is compatible for any table.
        #Store in arbitrary table; in this case A
        if len(known[startnode]) == 0:
            allvisited.add(startnode)
            A.add(startnode)
            seated[startnode]=2
            continue

        #'Open set' for DFS. Implemented as a dict for performance
        #If node X visited, visited[X]=True.
        visited = {}
        tovisit = set([startnode])
        parent[startnode] = startnode

        while len(tovisit)!=0:
            # Variant: len(tovisit)
            u = tovisit.pop()

            if not visited.get(u, False):
                #Node u has been visited
                allvisited.add(u)
                visited[u] = True
                startnodes.discard(u)

                #If parent node not seated at A, sit at A
                if seated[parent[u]]!=1:
                    seated[u]=1
                    A.add(u)
                #If parent node not seated at B, sit at B
                elif seated[parent[u]]!=2:
                    seated[u]=2
                    B.add(u)

                for v in known[u]:
                    #Variant: len(known)-known.index(v)
                    if v!=parent[u]:
                        tovisit.add(v)
                        #Set parent of v to u
                        parent[v]=u


    #Check if A or B contains incompatible guests.
    #If this is the case, it means that the problem is unsolvable
    for i in range(len(known)):
        # Variant: len(known)-i
        for j in known[i]:
            # Variant: len(known[i])-known[i].index(j)
            if i in A and j in A:
                return False, [], []
            elif i in B and j in B:
                return False, [], []

    return True, list(A),(B)


class PartySeatingTest(unittest.TestCase):
    """Test suite for party seating problem
    """

    def test_sanity(self):
        """Sanity test

        A minimal test case.
        """

        K=[[1,2],[0,2],[0,1]]
        (found, A, B) = party(K)
        self.assertEqual(
            len(A) + len(B),
            len(K),
            "wrong number of guests: {!s} guests, tables hold {!s} and {!s}".format(
                len(K),
                len(A),
                len(B)
                )
            )
        for g in range(len(K)):
            self.assertTrue(
                g in A or g in B,
                "Guest {!s} not seated anywhere".format(g))
        for a1 in A:
            for a2 in A:
                self.assertFalse(
                    a2 in K[a1],
                    "Guests {!s} and {!s} seated together, and know each other".format(
                        a1,
                        a2
                        )
                    )
        for b1 in B:
            for b2 in B:
                self.assertFalse(
                    b2 in K[b1],
                    "Guests {!s} and {!s} seated together, and know each other".format(
                        b1,
                        b2
                        )
                    )

if __name__ == '__main__':
    unittest.main()
