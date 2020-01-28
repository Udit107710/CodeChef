from collections import defaultdict

class Graph:
    def __init__(self, E, D, V):
        self.edgelist = defaultdict(list)
        self.edges = E
        self.directed = D
        self.vertices = V
        self.degree = defaultdict(list)
        self.elist = []

    def addedge(self, e1, e2, weight):
        self.edgelist[e1].append([e2, weight])
        if self.directed:
            return
        else:
            self.edgelist[e2].append([e1, weight])
        self.elist.append([e1,e2,weight])
    
    def prim_mst(self, start):
        in_tree = [False]*self.vertices
        distance = [1000000000]*self.vertices
        parent = [-1]*self.vertices

        distance[start] = 0
        k = start

        while(in_tree[k] == False):
            in_tree[k] = True
            for node in self.edgelist[k]:
                w = node[0]
                weight = node[1]
                if(distance[w] > weight) and (in_tree[w] == False):
                    distance[w] = weight
                    parent[w] = k
            k = 1
            dist = 1000000000
            for i in range(self.vertices):
                if(in_tree[i] == False) and (dist > distance[i]):
                    dist = distance[i]
                    k = i
            
        print(distance)

g1 = Graph(6, True, 4)
g1.addedge(0, 2, 30)
g1.addedge(1, 0, 22)
g1.addedge(1, 2, 10)
g1.addedge(2, 3, 20)
g1.addedge(3, 0, 16)
g1.addedge(3, 1, 5)
g1.prim_mst(2)
g1.prim_mst(0)
