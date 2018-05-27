#!/usr/bin/env python2

def matrix_chain_order(p):
    n = len(p) - 1

    m = [[0 for x in xrange(0, n)] for y in xrange(0, n)]
    s = [[0 for x in xrange(0, n)] for y in xrange(0, n)]

    for i in xrange(0,n):
        m[i][i] = 0

    # compute smallest matrix costs first
    # for chains of length 2 to n
    for l in xrange(2, n+1):
        for i in xrange(1, n - l + 1):
            j = i + l - 1 # j is the endpoint of the chain
            
            m[i][j] = float("inf")
            for k in xrange(i,j-1):
                q = m[i][k] + m[k+1][j] +  p[i] * p[k+1] * p[j+1]
                if q < m[i][j]:
                    m[i][j] =q
                    s[i][j] = k
            
            #if i < j: # skip the i > j cases since we must multiply in order
                # cost values
            #    c = [m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1] for k in xrange(i, j)]

                # get minimum index and value from costs
            #    (s[i][j], m[i][j]) = min(enumerate(c), key=lambda x: x[1])

            #    print i, j, [x for x in enumerate(c)]

            #    s[i][j] = s[i][j] + i + 1 # correct our s value (count from 1, offset by i because of enumerate)

    return m,s

def print_optimal_parens(s, i, j):
    if i == j:
        print "A_%d" % (i),
    else:
        print "(",
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j]+1, j)
        print ")",

m, s = matrix_chain_order([4,2,3,1,2])# 4,2,3,1,2

print_optimal_parens(s, 0,3)
