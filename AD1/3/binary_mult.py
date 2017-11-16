#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Binary Multiplication

Team Number: 100
Student Names: Lucas Herrera, Meriton Bytyqi
'''
import unittest

def binary_add(A,B):
    """
    Sig:    int[0..n-1], int[0..n-1] ==> int[0..n-1+amount]
    Pre: A and B must only contain elements within set S={0,1}
    Post: Sum of A and B in base 2
    Example:    binary_add([0,1],[0,1]) = [1,0]
    """
    A = ''.join(str(e) for e in A)
    B = ''.join(str(e) for e in B)
    bin_sum = bin(int(A,2)+int(B,2))

    result = list(bin_sum)
    result.remove('b')
    result = map(int,result)
    return(result)


def binary_shift(A, amount):
    """
    Sig:    int[0..n-1], int ==> int[0..n-1+amount]
    Pre: (none)
    Post: A appended with amount 0's
    Example:    binary_shift([0,1],2) = [0,1,0,0]
    """
    for i in range(amount):
        # Variant: amount - i
        A.append(0)
    return (A)

def binary_mult(A,B):
    """
    Sig:    int[0..n-1], int[0..n-1] ==> int[0..2*n-1]
    Pre: (none)
    Post: Product of A and B in base 2
    Var: Number of elements in A and B
    Example:    binary_mult([0,1,1],[1,0,0]) = [0,0,1,1,0,0]
    """

    #Boolean describing if original input lists A or B
    #have been modified in order to ensure that output product
    #is equal to 2*len(A)
    added = False

    if len(A)==1 & len(B)==1:
        #Recursion limit reached
        return ([A[0]*B[0]])

    #If input lists A or B were not a power of 2, prepend a 0
    if len(A)%2 != 0:
        A.insert(0,0)
        added=True
    if len(B)%2 != 0:
        B.insert(0,0)
        added=True

    input_size=len(A)

    al = A[0:(input_size/2)]
    ar = A[(input_size/2):input_size]

    bl = B[0:(input_size/2)]
    br = B[(input_size/2):input_size]

    a = binary_mult(al,bl)
    b = binary_mult(al,br)
    c = binary_mult(ar,bl)
    d = binary_mult(ar,br)

    x = binary_shift(a, input_size)
    y = binary_shift(binary_add(b,c), input_size/2)

    product = (binary_add(binary_add(x,y), d))

    #If input lists A or B were not originally a power of 2 and were modified,
    #undo the modification for satisfying that output is of size 2*input_size
    if added:
        input_size=input_size-1

    #Make length of product 2*input_size
    if len(product)!=2*input_size:
        if len(product)>2*input_size:
            while len(product)!=2*input_size:
                # Variant:  len(product) - 2*input_size
                del product[0]
        elif len(product)<2*input_size:
            while len(product)!=2*input_size:
                # Variant:  2*input_size - len(product)
                product.insert(0,0)

    return product
