parent = dict()
#rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
#    rank[vertice] = 0

def find(vertice):
    if parent[vertice] is vertice: return vertice
    parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    # with rank version
    # if root1 is root2: return
    # if rank[root1] < rank[root2]:
    #     parent[root1] = root2
    # else:
    #     parent[root2] = root1
    #     if rank[root1] is rank[root2]: rank[root1] += 1

    # without rank version
    if root1 is root2: return
    parent[root1] = root2

def kruskal(graph):
    for vertice in graph['vertices']:
    	make_set(vertice)
	minimum_spanning_tree = set()
	edges = graph['edges']
	edges.sort()
    for edge in edges:
    	weight, vertice1, vertice2 = edge
    	if find(vertice1) is not find(vertice2):
    	    union(vertice1, vertice2)
    	    minimum_spanning_tree.add(edge)

    return sorted(minimum_spanning_tree)

graph = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
'edges': [
(5, 'A', 'C'),
(20, 'A', 'B'),
(6, 'B', 'C'),
(3, 'B', 'D'),
(4, 'C', 'D'),
(3, 'C', 'E'),
(9, 'D', 'F'),
(1, 'C', 'F'),
(15, 'E', 'F'),]
}

print kruskal(graph)
