#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Binary Multiplication

Team Number: 
Student Names: 
'''
import unittest


def binary_mult(A,B):
    """
    Sig:    int[0..n-1], int[0..n-1] ==> int[0..2*n-1]
    Pre:    
    Post:   
    Var:    
    Example:    binary_mult([0,1,1],[1,0,0]) = [0,0,1,1,0,0]
    """
    
    if len(A)==1 && len(B)==1:
        return A[0]*B[0]

    if len(A)%2 != 0:
        A.insert(0,0)
    if len(B)%2 != 0:
        B.insert(0,0)
    
    
    A_l_half = A[0:(len(A)/2)]
    A_r_half = A[(len(A)/2):len(A)]

    B_l_half = B[0:(len(B)/2)]
    B_r_half = B[(len(B)/2):len(B)]
    
    binary_mult(A_r_half, B_r_half)
    binary_mult(A_l_half, B_l_half)
    


class BinaryMultTest(unittest.TestCase):
    """Test Suite for binary multiplication problem
    
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
        A = [0,1,1,0]
        B = [0,0,1,0]
        answer = binary_mult(A, B)
        self.assertEqual(answer, [0,0,0,0,1,1,0,0])

if __name__ == '__main__':
    unittest.main()

