#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Birthday Present

Team Number:
Student Names:
'''
import unittest

def birthday_present(P, n, t):
    '''
    Sig: int[0..n-1], int, int --> Boolean
    Pre:
    Post:
    Example: P = [2, 32, 234, 35, 12332, 1, 7, 56]
             birthday_present(P, len(P), 299) = True
             birthday_present(P, len(P), 11) = False
    '''
    # Initialize the dynamic programming matrix, A
    # Type: Int[0..n][0..t]
    A = [[None for i in range(t + 1)] for j in range(n + 1)]

    for i in range(n+1):
        A[i][0] = 0
    for i in range(t+1):
        A[0][i] = 0

    for r in range(1, n+1):
        for c in range(1, t+1):
            #Fel! A[r][c] ska vara weight[r]. sum(P[0:r])?
            if P[r-1] > c:
                A[r][c] = A[r-1][c]
            elif P[r-1] <= c:
                A[r][c] = max(P[r-1]+A[r-1][c-P[r-1]], A[r-1][c])

    return (A[-1][-1]==t)
def birthday_present_subset(P, n, t):
    '''
    Sig: int[0..n-1], int, int --> int[0..m]
    Pre:
    Post:
    Example: P = [2, 32, 234, 35, 12332, 1, 7, 56]
             birthday_present_subset(P, len(P), 299) = [56, 7, 234, 2]
             birthday_present_subset(P, len(P), 11) = []
    '''
    # Initialize the dynamic programming matrix, A
    # Type: Int[0..n][0..t]
    A = [[None for i in range(t + 1)] for j in range(n + 1)]

    for i in range(n+1):
        A[i][0] = 0
    for i in range(t+1):
        A[0][i] = 0

    for r in range(1, n+1):
        for c in range(1, t+1):
            #val[i]=weight[i]
            if P[r-1] > c:
                A[r][c] = A[r-1][c]
            elif P[r-1] <= c:
                A[r][c] = max(P[r-1]+A[r-1][c-P[r-1]], A[r-1][c])

    P_ = []
    if A[-1][-1] == t:
        c = t
        for r in range(n,-1,-1):
            if r == 0:
                break
            if A[r-1][c] < A[r][c]:
                P_.append(P[r-1])
                c = c-P[r-1]
    return (P_)


class BirthdayPresentTest(unittest.TestCase):
    """Test Suite for birthday present problem

    Any method named "test_something" will be run when this file is
    executed. Use the sanity check as a template for adding your own
    tests if you wish.
    (You may delete this class from your submitted solution.)
    """
    def test_sat_sanity_ez(self):
        """Sanity Test for birthday_present()

        This is a simple sanity check;
        passing is not a guarantee of correctness.
        """
        P = [1,5,6]
        n = len(P)
        t = 11
        #self.assertTrue(birthday_present(P, n, t))
    def test_sat_sanity(self):
        """Sanity Test for birthday_present()

        This is a simple sanity check;
        passing is not a guarantee of correctness.
        """
        P = [2,9,32, 234, 35, 12332, 1, 7, 56]
        n = len(P)
        t = 33
        #self.assertTrue(birthday_present(P, n, t))
    def test_sol_sanity(self):
        """Sanity Test for birthday_present_subset()

        This is a simple sanity check;
        passing is not a guarantee of correctness.
        """
        P = [2, 32, 234, 35, 12332, 1, 7, 56]
        n = len(P)
        t = 299
        self.assertTrue(birthday_present(P, n, t))
        self.assertItemsEqual(birthday_present_subset(P, n, t),
                              [56, 7, 234, 2])


if __name__ == '__main__':
    unittest.main()
