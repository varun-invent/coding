class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self,u,v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def BFS(self,s):
        # Array to store visited nodes
        visited = []

        # BFS uses a queue, so creating it
        queue = []

        # Starting with the source by appending it to the queue
        queue.append(s)
        visited.append(s)

        # Now start dequeuing and queuing the children nodes
        while queue:
            # Dequeue the first vertex
            s = queue.pop(0)
            print(s, end = " ")

            # Get all the adjacent nodes of the dewueued node
            if s not in self.graph:
                print()
                break
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)


# Driver Code

# Create a graph
g = Graph()
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(4,5)
g.addEdge(5,1)

s = 2
print(f'BFS Traversal starting from node {s}')
g.BFS(s)
