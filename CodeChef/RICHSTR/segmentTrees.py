
class Node(object):
    def __init__(self, *args, **kwargs):
        self.start = args[0]
        self.end = args[1]
        self.left = None
        self.right = None
        self.weight = None


class SegmentTree(object):

    def computeSum(self, l, r, node):
        print(node.start, node.end, node.weight, l, r)
        m = int((node.start + node.end)/2)
        if node.start == l and node.end == r:
            print("cond 1")
            return node.weight
        elif l > m and r > m:
            print("cond 2")
            return self.computeSum(l, r, node.right)
        elif l <= m and r <= m:
            print("cond 3")
            return self.computeSum(l, r, node.left)
        else:
            print("cond 4")
            return self.computeSum(l, m, node.left) + self.computeSum(m+1, r, node.right)
        
    def __init__(self, *args, **kwargs):
        self.root = None
    
    def addToTree(self, l, r, arr):
        node = Node(l,r)

        if r == len(arr) - 1:
            self.root = Node(l,r)
            node = self.root
        
        if l == r:
            node.weight = arr[l]
            return node
        else:
            m = int((l+r)/2)
            left, right = self.addToTree(l, m, arr), self.addToTree(m+1, r, arr)
            node.weight = left.weight + right.weight
            node.left = left
            node.right = right
            return node
            

tree = SegmentTree()
root = tree.addToTree(0, 4, [1,3,-2,8,-7])
print(root.left.right.weight)

sum = tree.computeSum(1, 3, root)
print(sum)