class Node(object):
    def __init__(self, val):
        super().__init__()
        self.value = val
        self.right = None
        self.left = None
        self.parent = None

class MinHeap(object):
    def __init__(self, val):
        super().__init__()
        self.root = Node(val)

    def add_node(self, val):
        queue = []
        node = [self.root, None]
        queue.insert(0, node)
        while queue:
            node = queue.pop(0)
            if node[0] is not None:
                queue.append([node[0].left, node[0]])
                queue.append([node[0].right, node[0]])
            else:
                break
        node[0] = Node(val)
        node[0].parent = node[1]
        if node[1].left is None:
            node[1].left = node[0]
        else:
            node[1].right = node[0]
        print(node[0].value, node[0].parent.value)
        self.heapify(node[0])

    def heapify(self, node: Node):
        while node is not self.root:
            if node.parent.value > node.value:
                temp = node.parent.value
                node.parent.value = node.value
                node.value = temp
                node = node.parent
            else:
                break

    def bfs(self):
        queue = []
        queue.insert(0, self.root)
        answer = []
        while queue:
            node = queue.pop(0)
            if node is not None:
                answer.append(node)
                queue.append(node.left)
                queue.append(node.right)
            else:
                answer.append(None)
            
        return answer
    
    def print(self):
        traversal = self.bfs()
        answer = [x.value if x is not None else None for x in traversal]
        print(*answer)

    def min(self):
        val = self.root.value
        node = self.root
        while node.left is not None and node.right is not None:
            if node.left.value < node.right.value:
                node.value = node.left.value
                node = node.left
                node.value = None
            else:
                node.value = node.right.value
                node = node.right
                node.value = None

        return val
        

heap = MinHeap(8)
heap.add_node(9)
heap.print()
heap.add_node(10)
heap.print()
heap.add_node(2)
heap.print()
heap.add_node(1)
heap.print()
heap.add_node(20)
heap.print()
heap.add_node(0)
heap.print()
heap.add_node(40)
heap.print()

print(heap.min())
heap.print()
print(heap.min())
heap.print()