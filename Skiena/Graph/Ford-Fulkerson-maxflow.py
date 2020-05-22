from collections import defaultdict

class Graph:

    def __init__(self, N):
        self.N = N
        self.edges = defaultdict(list)
    
    def add(self, p, q, w):
        self.edges[p].append([q,w])
    
    def bfs(self, start):
        queue = [start]
        traversed = []
        while queue:
            node = queue.pop(0)
            

        