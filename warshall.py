import pprint
def warshall(a):

    n = len(a)
    for i in range(n):
        for j in range(n):
            if i is j or a[i][j] is 1:
                a[i][j] = 1
            else:
                a[i][j] = 0


    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j] = a[i][j] or (a[i][k] and a[k][j])
    return a


graph = [
        [0,1,0,0,1,1,0,1],
        [0,0,1,0,0,0,1,0],
        [0,0,0,1,0,0,1,0],
        [0,0,0,0,0,1,0,0],
        [0,0,1,0,0,1,0,0],
        [0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,1,1,0],
        ]
pprint.pprint(warshall(graph))
