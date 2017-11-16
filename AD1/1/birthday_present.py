#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Birthday Present

Team Number: 100
Student Names: Lucas Herrera, Meriton Bytyqi
'''
import unittest

def birthday_present(P, n, t):
    '''
    Sig: int[0..n-1], int, int --> Boolean
    Pre: n must be equal to the length of P,
         t must be a non-negative integer
    Post: True if there exists solution to given birthday problem,
          False otherwise
    Example: P = [2, 32, 234, 35, 12332, 1, 7, 56]
             birthday_present(P, len(P), 299) = True
             birthday_present(P, len(P), 11) = False
    '''
    # Initialize the dynamic programming matrix, A
    # Type: Int[0..n][0..t]
    A = [[None for i in range(t + 1)] for j in range(n + 1)]

    #Set all values of the first column of A to 0
    for i in range(n+1):
        # Variant:  (n+1) - i
        A[i][0] = 0

    #Iterate through every element of A and calculate
    #the sum of optimally picked prices from P given current price limit (p).
    #Store the results in A.
    for i in range(0, n+1):
        # Variant:  (n+1) - i
        for p in range(0, t+1):
            # Variant: (t+1) - p
            if i == 0:
                A[i][p] = 0
            elif P[i-1] > p:
                A[i][p] = A[i-1][p]
            elif P[i-1] <= p:
                A[i][p] = max(P[i-1]+A[i-1][p-P[i-1]], A[i-1][p])

    #If A[n][t] = t, there exists a subset P' of P
    #that contains prices with a total sum of t.
    #Return True in that case, else False.
    return (A[n][t]==t)
def birthday_present_subset(P, n, t):
    '''
    Sig: int[0..n-1], int, int --> int[0..m]
    Pre: Pre: n must be equal to the length of P,
              t must be a non-negative integer
    Post: List of prices in P that sum up to exactly t
          if there exists solution to given birthday problem,
          [] otherwise
    Example: P = [2, 32, 234, 35, 12332, 1, 7, 56]
             birthday_present_subset(P, len(P), 299) = [56, 7, 234, 2]
             birthday_present_subset(P, len(P), 11) = []
    '''
    # Initialize the dynamic programming matrix, A
    # Type: Int[0..n][0..t]
    A = [[None for i in range(t + 1)] for j in range(n + 1)]

    #Set all values of the first column of A to 0
    for i in range(n+1):
        # Variant:  (n+1) - i
        A[i][0] = 0

    #Iterate through every element of A and calculate
    #the sum of optimally picked prices from P given current price limit (p).
    #Store the results in A.
    for i in range(0, n+1):
        # Variant:  (n+1) - i
        for p in range(0, t+1):
            # Variant: (t+1) - p
            if i == 0:
                A[i][p] = 0
            elif P[i-1] > p:
                A[i][p] = A[i-1][p]
            elif P[i-1] <= p:
                A[i][p] = max(P[i-1]+A[i-1][p-P[i-1]], A[i-1][p])

    #Initialize the subset P'
    #Type: Int[]
    P_ = []

    #If there exists a subset P' of P
    #whose sum is exactly equal to t,
    #insert the prices of this subset into P_
    if A[n][t] == t:
        #Let p denote the current price limit
        p = t
        for i in range(n,-1,-1):
            # Variant: i
            if i == 0:
                break
            if A[i-1][p] < A[i][p]:
                P_.append(P[i-1])
                p = p-P[i-1]
    return (P_)
