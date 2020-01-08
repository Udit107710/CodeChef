from collections import defaultdict

class Graph:
    def __init__(self, N):
        self.N = N
        self.graph = defaultdict(list)

    def addEdge(self, v, u):
        self.graph[v].append(u)
        self.graph[u].append(v)
    
    def isCycle(self, node, parent, visited):
        visited[node] = True

        for n in self.graph[node]:
            if visited[n] == False:
                if self.isCycle(n, node, visited) == True:
                    return True
            elif n is not parent:
                return True
        return False

    def isTree(self):
        visited = [False] * self.N

        if self.isCycle(0, -1, visited) is True:
            return False
        
        for value in visited:
            if value == False:
                return False

        return True

g1 = Graph(5) 
g1.addEdge(1, 0) 
g1.addEdge(0, 2) 
g1.addEdge(0, 3) 
g1.addEdge(3, 4)

print(g1.isTree())

g2 = Graph(5) 
g2.addEdge(1, 0) 
g2.addEdge(0, 2) 
g2.addEdge(2, 1) 
g2.addEdge(0, 3) 
g2.addEdge(3, 4) 

print(g2.isTree())
