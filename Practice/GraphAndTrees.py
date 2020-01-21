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
    
    def bfs(self, k):
        visited = [False] * self.N
        queue = [k]
        array = []
        while queue:
            node = queue.pop(0)
            visited[node] = True
            for n in self.graph[node]:
                if not visited[n]:
                    queue.append(n)
            array.append(node)
        return array
    
    def dfs(self, k):
        visited = [False] * self.N
        stack = [k]
        array = []
        while stack:
            node = stack.pop(-1)
            array.append(node)
            visited[node] = True
            for n in self.graph[node]:
                if not visited[n]:
                    stack.append(n)
        return array

g1 = Graph(7) 
g1.addEdge(1, 0) 
g1.addEdge(0, 2) 
g1.addEdge(0, 3) 
g1.addEdge(3, 4)
g1.addEdge(2, 5)
g1.addEdge(1, 6)

print(g1.isTree())
print(g1.graph)
print(g1.bfs(0))
print(g1.dfs(0))

g2 = Graph(5) 
g2.addEdge(1, 0) 
g2.addEdge(0, 2) 
g2.addEdge(2, 1) 
g2.addEdge(0, 3) 
g2.addEdge(3, 4) 

print(g2.isTree())
print(g2.graph)
print(g2.bfs(0))
print(g2.dfs(0))