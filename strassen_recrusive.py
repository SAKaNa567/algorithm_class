import random
import time

def add(a, b):
    length = len(a)
    c = [[0 for x in range(length)] for y in range(length)]

    for i in xrange(0, length):
        for j in xrange(0, length):
            c[i][j] = a[i][j] + b[i][j]

    return c


def subtract(a, b):
    length = len(a)
    c = [[0 for x in range(length)] for y in range(length)]

    for i in xrange(0, length):
        for j in xrange(0, length):
            c[i][j] = a[i][j] - b[i][j]

    return c


def rand_num_filler(a):
    length = len(a) ** 2
    filled_matrix = [[0 for x in range(length)] for y in range(length)]

    for i in xrange(0, length):
        for j in xrange(0, length):
            random.seed(2016)
            rand_int = random.randrange(1, 100)
            filled_matrix[i][j] = rand_int

    return filled_matrix


def regular_multiplication(a, b):
    length = len(a)
    c = [[0 for x in range(length)] for y in range(length)]

    for i in xrange(0, length):
        for j in xrange(0, length):
            for k in xrange(0, length):
                c[i][j] += a[i][k] * b[k][j]

    return c


def strassen_multiplication(a, b):
    length = len(a)
    c = [[0 for x in range(length)] for y in range(length)]

    leaf = 128
    if length < leaf:
        return regular_multiplication(a, b)
    else:
        a11 = [[0 for x in range(length / 2)] for y in range(length / 2)]
        a12 = [[0 for x in range(length / 2)] for y in range(length / 2)]
        a21 = [[0 for x in range(length / 2)] for y in range(length / 2)]
        a22 = [[0 for x in range(length / 2)] for y in range(length / 2)]
        b11 = [[0 for x in range(length / 2)] for y in range(length / 2)]
        b12 = [[0 for x in range(length / 2)] for y in range(length / 2)]
        b21 = [[0 for x in range(length / 2)] for y in range(length / 2)]
        b22 = [[0 for x in range(length / 2)] for y in range(length / 2)]

        for i in xrange(0, length / 2):
            for j in xrange(0, length / 2):
                a11[i][j] = a[i][j]
                a12[i][j] = a[i][j + (length / 2)]
                a21[i][j] = a[i + (length / 2)][j]
                a22[i][j] = a[i + (length / 2)][j + (length / 2)]
                b11[i][j] = b[i][j]
                b12[i][j] = b[i][j + (length / 2)]
                b21[i][j] = b[i + (length / 2)][j]
                b22[i][j] = b[i + (length / 2)][j + (length / 2)]

        p1 = strassen_multiplication(a11, subtract(b12, b22))
        p2 = strassen_multiplication(add(a11, a12), b22)
        p3 = strassen_multiplication(add(a21, a22), b11)
        p4 = strassen_multiplication(a11, subtract(b21, b11))
        p5 = strassen_multiplication(add(a11, a22), add(b11, b12))
        p6 = strassen_multiplication(subtract(a12, a22), add(b21, b22))
        p7 = strassen_multiplication(subtract(a11, a21), add(b11, b12))

        c11 = add(subtract(add(p5, p4), p2), p6)  # c11 = p5 + p4 - p2 + p6
        c12 = add(p1, p2)  # c12 = p1 + p2
        c21 = add(p3, p4)  # c21 = p3 + p4
        c22 = subtract(subtract(add(p5, p1), p3), p7)  # c22 = p5 + p1 - p3 - p7

        for i in xrange(0, length / 2):
            for j in xrange(0, length / 2):
                c[i][j] = c11[i][j]
                c[i][j + (length / 2)] = c12[i][j]
                c[i + (length / 2)][j] = c21[i][j]
                c[i + (length / 2)][j + (length / 2)] = c22[i][j]

        return c

import numpy as np

def matrix_mul(A,B):

    if A.shape == (1,1):
        return A.dot(B)

    else:

        dim = A.shape[0]//2

        X1 = matrix_mul(A[:dim,:dim],B[:dim,:dim]) # A11 B11
        X2 = matrix_mul(A[:dim,dim:],B[dim:,:dim]) # A12 B21
        X3 = matrix_mul(A[:dim,:dim],B[:dim,dim:]) # A11 B12
        X4 = matrix_mul(A[:dim,dim:],B[dim:,dim:]) # A12 B22

        X5 = matrix_mul(A[dim:,:dim],B[:dim,:dim]) # A21 B11
        X6 = matrix_mul(A[dim:,dim:],B[dim:,:dim]) # A22 B21
        X7 = matrix_mul(A[dim:,:dim],B[:dim,dim:]) # A21 B12
        X8 = matrix_mul(A[dim:,dim:],B[dim:,dim:]) # A22 B22

        C = np.empty((2*dim,2*dim))

        C[:dim,:dim] = X1 + X2
        C[:dim,dim:] = X3 + X4
        C[dim:,:dim] = X5 + X6
        C[dim:,dim:] = X7 + X8

        print (C)

        return C








#strassen version
test_size = 32

A = [[0] * test_size for i in range(test_size)]
A = rand_num_filler(A)

B = [[0] * test_size for i in range(test_size)]
B = rand_num_filler(B)


start_strassen = time.clock()
m2 = strassen_multiplication(A, B)
end_strassen = time.clock()
print("strassen Multiplication: " + str(end_strassen - start_strassen) + " seconds")


#recursive version
A2 = np.asarray([[1+j*dim+i for i in range(test_size)] for j in range(test_size)])
B2 = np.asarray([[1+j*dim+i for i in range(test_size)] for j in range(test_size)])


start_recursive2 = time.clock()
m2 = matrix_mul(A2, B2)
end_recursive2 = time.clock()
print("recursive Multiplication: " + str(end_recursive2 - start_recursive2) + " seconds")
