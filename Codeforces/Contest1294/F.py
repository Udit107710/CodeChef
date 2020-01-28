from sys import stdin
from collections import defaultdict

class Graph:
    def __init__(self, N):
        self.adj = defaultdict(list)
        self.N = N
    
    def add_edge(e1, e2):
        self.adj[e1].append(e2)
        self.adj[e2].append(e1)
    
    def cal():
        