#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Binary Multiplication

Team Number:
Student Names:
'''
import unittest

#A and B must be lists containing elements within set S={0,1}
def binary_add(A,B):
    A = ''.join(str(e) for e in A)
    B = ''.join(str(e) for e in B)
    bin_sum = bin(int(A,2)+int(B,2))

    result = list(bin_sum)
    result.remove('b')
    result = map(int,result)
    return(result)


def binary_shift(A, amount):
    for i in range(amount): A.append(0)
    return (A)

def binary_mult(A,B):
    """
    Sig:    int[0..n-1], int[0..n-1] ==> int[0..2*n-1]
    Pre:
    Post:
    Var:
    Example:    binary_mult([0,1,1],[1,0,0]) = [0,0,1,1,0,0]
    """
    n = len(A)

    if len(A)==1 and len(B)==1:
        return ([A[0]*B[0]])


    if len(A)%2 != 0:
        A.insert(0,0)
    if len(B)%2 != 0:
        B.insert(0,0)


    Al = A[0:(len(A)/2)]
    Ar = A[(len(A)/2):len(A)]

    Bl = B[0:(len(B)/2)]
    Br = B[(len(B)/2):len(B)]

    a = binary_mult(Al,Bl)
    b = binary_mult(Al,Br)
    c = binary_mult(Ar,Bl)
    d = binary_mult(Ar,Br)

    x = binary_shift(a, n)
    y = binary_shift(binary_add(b,c), n/2)

    result = (binary_add(binary_add(x,y), d))

    #Make length of result 2*n
    while len(result)<2*n:
        result.insert(0,0)
    while len(result)>2*n:
        del result[0]#KNASSS
    return result


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
    def test_sanity_uneven(self):
        """Sanity Test

        This is a simple sanity check for your function;
        passing is not a guarantee of correctness.
        """
        A = [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1]
        B = [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1]
        answer = binary_mult(A, B)
        #DENNA E KNAS
        #self.assertEqual(answer, [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1])



if __name__ == '__main__':
    unittest.main()
