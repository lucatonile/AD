#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Integer Sort

Team Number: 100
Student Names: Lucas Herrera, Meriton Bytyqi
'''
import unittest

def integer_sort(A, k):
    '''
    Sig: int array[1..n], int -> int array[1..n]
    Pre: k must be value of highest element in A
    Post: A[1..n] is a non-decreasingly ordered permutation of its original elements
    Example: integer_sort([5, 3, 6, 7, 12, 3, 6, 1, 4, 7]), 12) =
                 [1, 3, 3, 4, 5, 6, 6, 7, 7, 12]
    '''
    # Initialize the auxilliary integer array, Y
    # Type: Int[0..k]
    Y = [0]*(k+1)

    #Scan A for all indices i: if A[i] = x, then increment Y[x] by 1.
    for i in range(0, len(A)):
        # Variant:  len(A) - i
        Y[A[i]] = Y[A[i]]+1

    #Empty A
    del A[:]

    #Scan Y for all indices x:
    #if Y[x] = t > 0, then record value x a total of t times into A
    for x in range(0, k+1):
        # Variant:  (k+1) - x
        if Y[x] > 0:
            for i in range(Y[x]):
                # Variant:  Y[x] - i
                # Append value x into A
                A.append(x)
    return(A)
