def node_distance(grid, node, distance):
    if distance == 1:
        nodes = []
        for p in range(len(grid)):
            for q in range(len(grid)):
                if p == node and grid[p][q] == 1:
                    nodes.append(q)
        #print("distance is 1")
        #print(nodes)
        return nodes
    else:
        nodes = []
        for p in range(len(grid)):
            for q in range(len(grid)):
                if p == node and grid[p][q] == 1:
                    nodes.append(q)
        answers = []
        #print("distance is", distance)
        #print(nodes)
        for n in nodes:
            answers.extend(node_distance(grid, n, distance-1))
        return answers


T = int(input())
for _ in range(T):
    n, q = map(int, input().split())
    nodes = [[0 for i in range(n)] for j in range(n)] 
    for __ in range(n-1):
        i, j = map(int, input().split())
        nodes[i-1][j-1] = 1
        nodes[j-1][i-1] = 1
    for ___ in range(q):
        a, da, b, db = map(int, input().split())
        #print("#1")
        a_nodes = set(node_distance(nodes, a-1, da))
        a_nodes = set(filter(lambda p: p != a, a_nodes))
        #print("#2")
        b_nodes = set(node_distance(nodes, b-1, db))
        b_nodes = set(filter(lambda a: a != b, b_nodes))
        intersect = a_nodes.intersection(b_nodes)
        if len(intersect) > 0:
            print(intersect.pop()+1)
        else:
            print(-1)


