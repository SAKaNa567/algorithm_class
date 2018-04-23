import pprint
simple_graph = {
    '1': ['2','4'],
    '2': ['5'],
    '3': ['5','6'],
    '4': ['2'],
    '5': ['4'],
    '6': ['6']
}

graph = {}
time_s = 0

def DFS_visit(i):
    global time_s
    time_s = time_s + 1
    graph[i]['discovery_time'] = time_s
    graph[i]['color'] = 'Gray'
    for j in simple_graph[i]:
        if graph[j]['color'] == 'white':
            DFS_visit(j)
    graph[i]['color'] = 'Black'
    time_s = time_s + 1
    graph[i]['finished_time'] = time_s



def DFS():
    for i in simple_graph.keys():
        graph[i] = {'color':'white'}
    for i in simple_graph.keys():
        if graph[i]['color'] == 'white':
            DFS_visit(i)

DFS()
pprint.pprint(graph)
