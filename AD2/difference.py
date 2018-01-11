#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 2: Search String Replacement

Team Number:
Student Names:
'''
import unittest
# Sample matrix provided by us:
from string import ascii_lowercase

# Solution to part b:
def min_difference(u,r,R):
    """
    Sig:    string, string, int[0..|A|, 0..|A|] ==> int
    Pre:
    Post:
    Example: Let R be the resemblance matrix where every change and skip costs 1
             min_difference("dinamck","dynamic",R) ==> 3
    """
    # To get the resemblance between two letters, use code like this:
    # difference = R['a']['b']

    # Initialize the dynamic programming matrix, A
    # Type: Int[0..n][0..t]
    A = [[None for i in range(len(r)+1)] for j in range(len(u)+1)]

    #Set all values of the first column of A to 0
    A[0][0]=0

    #Initialize every element in row 0 of the dynamic programming matrix.
    for i in range(1,len(r)+1):
        # Variant:  (r+1) - i
        A[0][i] = A[0][i-1] + R['-'][r[i-1]]

    #Initialize every element in column 0 of the dynamic programming matrix.
    for i in range(1,len(u)+1):
        # Variant:  (u+1) - i
        A[i][0] = A[i-1][0] + R[u[i-1]]['-']

    #Compute dynamic programming matrix
    for i in range(1, len(u)+1):
        # Variant:  (n+1) - i
        for j in range(1, len(r)+1):
            #Get value of min-cost operation
            A[i][j]= min(A[i-1][j] + R[u[i-1]]['-'],
                A[i][j-1] + R['-'][r[j-1]],
                A[i-1][j-1] + R[u[i-1]][r[j-1]])

    return A[-1][-1]
# Solution to part c:
def min_difference_align(u,r,R):
    """
    Sig:    string, string, int[0..|A|, 0..|A|] ==> int, string, string
    Pre:
    Post:
    Example: Let R be the resemblance matrix where every change and skip costs 1
             min_difference_align("dinamck","dynamic",R) ==>
                                    3, "dinam-ck", "dynamic-"
    """

    # Initialize the operation matrix. Every element describes operation performed
    # in dynamic programming matrix
    # Type: Str[0..n][0..t]
    ops=[['' for i in range(len(r)+1)] for j in range(len(u)+1)]

    # Initialize the dynamic programming matrix, A
    # Type: Int[0..n][0..t]
    A = [[None for i in range(len(r)+1)] for j in range(len(u)+1)]

    #Set all values of the first column of A to 0
    A[0][0]=0

    #Initialize every element in column 0 of the dynamic programming matrix.
    for i in range(1,len(u)+1):
        # Variant:  (u+1) - i
        A[i][0] = A[i-1][0] + R[u[i-1]]['-']

    #Initialize every element in row 0 of the dynamic programming matrix.
    for i in range(1,len(r)+1):
        # Variant:  (r+1) - i
        A[0][i] = A[0][i-1] + R['-'][r[i-1]]

    #Initialize every element in column 0 of the operations matrix.
    for i in range(1,len(u)+1):
        # Variant:  (u+1) - i
        ops[i][0] = 'r_skip'

    #Initialize every element in row 0 of the operations matrix.
    for i in range(1,len(r)+1):
        # Variant:  (r+1) - i
        ops[0][i] = 'u_skip'

    #Compute dynamic programming matrix
    for i in range(1, len(u)+1):
        # Variant:  (u+1) - i
        for j in range(1, len(r)+1):
            # Variant:  (r+1) - i
            #Save min-cost operation for backtrack.
            op = {'r_skip': A[i-1][j] + R[u[i-1]]['-'],
                'u_skip': A[i][j-1] + R['-'][r[j-1]],
                'u_alter': A[i-1][j-1] + R[u[i-1]][r[j-1]]}
            #Get value of min-cost operation
            A[i][j]= min(op.itervalues())
            #Save min-cost operation in operations matrix
            ops[i][j]=(min(op,key=op.get))

    #Backtrack in dunamic programming matrix to retrieve optimal path
    i = len(u)
    j = len(r)

    #Alignment strings
    u_ = ""
    r_ = ""

    #List containing optimal operations performed in order to achieve string positioning
    path = []

    #Construct path
    while i+j!=0:
        # Variant: len(u)*len(r) - (i+j)
        path.insert(0,ops[i][j])
        if ops[i][j]=='r_skip':
            i-=1
        elif ops[i][j]=='u_skip':
            j-=1
        elif ops[i][j]=='u_alter':
            i-=1
            j-=1

    #Construct string positionings using path
    i = 0
    j = 0
    for op in path:
        # Variant: len(path) - path.index(op)
        if op=='r_skip':
            u_+=u[i]
            r_+='-'
            i+=1
        elif op=='u_skip':
            u_ += '-'
            r_ += r[j]
            j+=1
        elif op=='u_alter':
            u_+=u[i]
            r_+=r[j]
            i+=1
            j+=1
    return A[-1][-1], u_, r_

def qwerty_distance():
    """Generates a QWERTY Manhattan distance resemblance matrix

    Costs for letter pairs are based on the Manhattan distance of the
    corresponding keys on a standard QWERTY keyboard.
    Costs for skipping a character depends on its placement on the keyboard:
    adding a character has a higher cost for keys on the outer edges,
    deleting a character has a higher cost for keys near the middle.

    Usage:
        R = qwerty_distance()
        R['a']['b']  # result: 5
    """
    from collections import defaultdict
    import math
    R = defaultdict(dict)
    R['-']['-'] = 0
    zones = ["dfghjk", "ertyuislcvbnm", "qwazxpo"]
    keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    for num, content in enumerate(zones):
        for char in content:
            R['-'][char] = num + 1
            R[char]['-'] = 3 - num
    for a in ascii_lowercase:
        rowA = None
        posA = None
        for num, content in enumerate(keyboard):
            if a in content:
                rowA = num
                posA = content.index(a)
        for b in ascii_lowercase:
            for rowB, contentB in enumerate(keyboard):
                if b in contentB:
                    R[a][b] = math.fabs(rowB - rowA) + math.fabs(posA - contentB.index(b))
    return R
