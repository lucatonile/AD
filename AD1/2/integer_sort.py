#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Integer Sort

Team Number: 100
Student Names: Meriton Bytyqi & Lucas Herrera
'''
import unittest

def integer_sort(A, k):
    '''
    Sig: int array[1..n], int -> int array[1..n]
    Pre:
    Post:
    Example: integer_sort([5, 3, 6, 7, 12, 3, 6, 1, 4, 7]), 12) =
                 [1, 3, 3, 4, 5, 6, 6, 7, 7, 12]
    '''
# Creates an auxiliary integer array Y [0..k] and initialise it with zeros.
    Y = [0]*(k+1)
# Scans A for all indices i: if A[i] = x, then increments Y [x] by 1.
    for i in range(0, len(A)):
        Y[A[i]] = Y[A[i]]+1
    A = []
# Scans Y for all indices x: if Y [x] = t > 0, then records value x a total of t times into A. 
    for x in range(0, k+1):
        if Y[x] > 0:
            for i in xrange(Y[x]):
                A.append(x)
# Returns A
    return(A)

class IntegerSortTest(unittest.TestCase):
    """Test Suite for integer sort problem

    Any method named "test_something" will be run when this file is
    executed. Use the sanity check as a template for adding your own
    tests if you wish.
    (You may delete this class from your submitted solution.)
    """

    def test_sanity(self):
        """Sanity Test

        This is a simple sanity check for your function;
        passing is not a guarantee of correctness.
        """
        A = [5, 3, 6, 7, 12, 3, 6, 1, 4, 7]
        R = integer_sort(A, 12)
        self.assertEqual(R, [1, 3, 3, 4, 5, 6, 6, 7, 7, 12])

if __name__ == '__main__':
    unittest.main()
