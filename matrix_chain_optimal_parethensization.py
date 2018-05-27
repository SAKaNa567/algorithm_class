def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for x in xrange(0, n)] for y in xrange(0, n)]
    s = [[0 for x in xrange(2, n+1)] for y in xrange(1, n)]
    for i in xrange(0,n):
        m[i][i] = 0
    for l in xrange(2, n+1):
        for i in xrange(0, n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in xrange(i,j):
                q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i-1][j-1] = k
    return m,s

alpha = ['A','B','C','D','E','F']
def print_optimal_parens(s, i, j):
    if i == j:
        print alpha[i] ,
    else:
        print "(",
        print_optimal_parens(s, i, s[i-1][j-1])
        print_optimal_parens(s, s[i-1][j-1]+1, j)
        print ")",

m, s = matrix_chain_order([130,35,15,5,10,20,25])
print "Problem A =",
print_optimal_parens(s, 0, 5)
print " "
print "Problem B =",
m, s = matrix_chain_order([10,20,10,15,20,10])
print_optimal_parens(s, 0, 4)
print " "

print "Problem C =",
m, s = matrix_chain_order([100,10,100,1,1000,100])
print_optimal_parens(s, 0, 4)
