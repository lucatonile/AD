#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Integer Sort

Team Number:
Student Names:
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
    Y = [0]*(k+1)

    for i in range(0, len(A)):
        Y[A[i]] = Y[A[i]]+1
    A = []
    for x in range(0, k+1):
        if Y[x] > 0:
            for i in xrange(Y[x]):
                A.append(x)
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
