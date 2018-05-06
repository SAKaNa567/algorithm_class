# coding: utf-8
graph  = {
    "0":{
        "1":5,
        "7":8,
        "4":9,
    },
    "1":{
        "7":4,
        "3":15,
    },
    "2":{
        "3":3,
        "6":11,
    },
    "3":{
        "6":9,
    },
    "4":{
        "7":5,
        "5":4,
        "6":20,
    },
    "5":{
        "6":13,
        "2":1,
    },
    "6":{

    },
    "7":{
        "2":7,
        "5":6,
    },
}

d = {}

def heap_push(pq,li):
    pq.append(li)
    pq.sort()

def heap_pop():
    tmp = pq[0]
    pq.remove(pq[0])
    return tmp

pq = []
def dijkstra(s):
    for i in range(len(graph)):
        d[str(i)] = float('inf')
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

print dijkstra("0")
