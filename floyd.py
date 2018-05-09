import pprint
def floyd(A):
    n = len(A)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if A[i][k]+A[k][j]<A[i][j]:
                    A[i][j]=A[i][k]+A[k][j]
    return A

inf = float('inf')
graph = [
    [0,48,inf,8,20,inf,20,inf],
    [inf,0,24,inf,9,inf,76,29],
    [97,inf,0,inf,inf,inf,18,1],
    [inf,52,34,0,29,inf,inf,inf],
    [inf,inf,inf,inf,0,10,inf,inf],
    [inf,10,85,43,inf,0,41,29],
    [inf,inf,inf,76,38,inf,0,inf],
    [28,42,inf,77,21,inf,11,0],
]
pprint.pprint(floyd(graph))
