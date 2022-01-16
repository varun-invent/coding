class Graph:
    def __init__(self):
        # Representing a graph by adjacency list stored in
        # the form of a dictionary
        self.graph = {}

    def addEdge(self,u,v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def BFS(self,s):
        res = [] # Restlt
        # Do BFS starting from a source node
        # Define a queue
        queue = []
        
        # Define a visited list to keep track of visited nodes
        visited = []

        queue.append(s)
        visited.append(s)
        
        # Iterate over the queue
        while queue:
            s = queue.pop(0)
            print(s, end = " ")
            res.append(s)
            if s not in self.graph:
                break
                print()
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)

        return res
# Driver code add edges to the graph

g = Graph()

edges = [(1,2),
        (3,4),
        (4,5),
        (5,1),
        (6,7),
        (7,8),
        (5,6),
        (10,11),
        (12,13)
        ]

all_nodes = []

# Undirected graph
for u,v in edges:
    g.addEdge(u,v)
    g.addEdge(v,u)
    
    if u not in all_nodes:
        all_nodes.append(u)
    if v not in all_nodes:
        all_nodes.append(v)


print(all_nodes)
n_components = 0
while all_nodes:
    res = g.BFS(list(all_nodes)[0])
    remaining_nodes = set(all_nodes) - set(res)
    all_nodes = remaining_nodes
    n_components = n_components+1

print()
print(f'Number of components {n_components}')
