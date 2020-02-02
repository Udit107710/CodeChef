from collections import defaultdict

class SetUnion:
    def __init__(self, n):
        self.n = n
        self.p = [i for i in range(n)]
        self.size = [1]*n

    def find(self, i):
        if self.p[i] == i:
            return i
        else:
            return self.find(self.p[i])
    
    def union(self, i, j):
        r1 = self.find(i)
        r2 = self.find(j)

        if r1 == r2:
            return
        
        if self.size[r1] >= self.size[r2]:
            self.size[r1] += self.size[r2]
            self.p[r2] = r1
        else:
            self.size[r2] += self.size[r2]
            self.p[r1] = self.p[r2]

class Graph:
    def __init__(self, E, D, V):
        self.edgelist = defaultdict(list)
        self.edges = E
        self.directed = D
        self.vertices = V
        self.degree = defaultdict(list)
        self.elist = [] # Only for Kruskal

    def addedge(self, e1, e2, weight):
        self.elist.append([e1,e2,weight]) # Not for prim's
        self.edgelist[e1].append([e2, weight])
        if self.directed:
            return
        else:
            self.edgelist[e2].append([e1, weight])
    
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

    def kruskal_mst(self):
        cost = 0
        set_union = SetUnion(self.vertices)
        print(self.elist)
        sorted_elist = sorted(self.elist, key= lambda x:x[2])
        print(sorted_elist)
        for i in range(len(sorted_elist)):
            node = sorted_elist.pop(0)
            print(set_union.p, node)
            if set_union.find(node[0]) != set_union.find(node[1]):
                cost += node[2]
                set_union.union(node[0], node[1])
        return cost

g1 = Graph(6, True, 4)
g1.addedge(0, 2, 30)
g1.addedge(1, 0, 22)
g1.addedge(1, 2, 10)
g1.addedge(2, 3, 20)
g1.addedge(3, 0, 16)
g1.addedge(3, 1, 5)
g1.prim_mst(2)
g1.prim_mst(0)
print(g1.kruskal_mst())
