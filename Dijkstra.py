# coding: utf-8
graph = {
    "A":{
        "B":    20,
        "C":    5,
        "E":    1,
        },
    "B":{
        "E":    10,
    },
    "C":{
        "D":    13,
    },
    "D":{

    },
    "E":{
        "D":    4,
    },
}

d = {
    "A":float('inf'),
    "B":float('inf'),
    "C":float('inf'),
    "D":float('inf'),
    "E":float('inf'),
}
def heap_push(pq,li):
    pq.append(li)
    pq.sort()

def heap_pop():
    tmp = pq[0]
    pq.remove(pq[0])
    return tmp

pq = []
def dijkstra(s):
    # d=[float('inf')]*6
    d[s]=0
    heap_push(pq,[0,s])
    while len(pq) is not 0:
        t,u=heap_pop()#EXTRACT_MINの役割を果たしています。下のforで行われた中で一番小さいものがremoveされます。
        # if d[u] is not t:
            # continue
        if d[u] is float('inf'):
            break
        for v in graph[u].keys():#例）このループでg["A"]のkeys全てを調べる
            if d[u]+graph[u][v]<d[v]:
                d[v]=d[u]+graph[u][v]#上書き処理
                heap_push(pq,[d[v],v])#[w,"B"],[w,"C"]..etc.¥
    return d

print dijkstra("A")
