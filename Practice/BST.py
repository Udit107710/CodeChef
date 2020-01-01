class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BST:
    def __init__(self, root):
        self.root = Node(root)
    
    def insert(self, value, node = None):
        if node is None:
            node = self.root
        if node.value >= value:
            if node.left == None:
                node.left = Node(value)
            else:
                self.insert(value, node.left)
        else:
            if node.right == None:
                node.right = Node(value)
            else:
                self.insert(value, node.right)
    def dfs(self):
        stack = [self.root]

        while stack:
            node = stack.pop()
            if node is not None:
                print(node.value, "->", end=" ")
                stack.append(node.right)
                stack.append(node.left)
            else:
                print("leaf", " ->", end=" ")
        
    def bfs(self):
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            if node is not None:
                print(node.value, "->",end=" ")
                queue.append(node.left)
                queue.append(node.right)
            else:
                print("leaf", end=" ")

    def traversal(self):
        inOrder = self.inOrder(self.root)
        postOrder = self.postOrder(self.root)
        preOrder = self.preOrder(self.root)

        print(inOrder)
        print(postOrder)
        print(preOrder)

    def preOrder(self, node):
        order = [node.value]

        if node.left is not None:
            order.extend(self.preOrder(node.left))
       
        if node.right is not None:
            order.extend(self.preOrder(node.right))
        
        return order

    def postOrder(self, node):
        order = []

        if node.left is not None:
            order.extend(self.postOrder(node.left))
        
        
        if node.right is not None:
            order.extend(self.postOrder(node.right))
       

        order.append(node.value)
        
        return order
    
    def inOrder(self, node):
        order = []

        if node.left is not None:
            order.extend(self.inOrder(node.left))
        
        order.append(node.value)
        
        if node.right is not None:
            order.extend(self.inOrder(node.right))
        
        return order
    
    def check_foldable(self):
        return self.foldlable(self.root.left, self.root.right)
    
    def foldlable(self, left, right):
        if left is None and right is None:
            return True
        elif left is None:
            return False
        elif right is None:
            return False
        else:
            return all([self.foldlable(left.left, right.right), self.foldlable(left.right, right.left)])

bst = BST(9)
bst.insert(4)
bst.insert(12)
bst.insert(3)
bst.insert(10)
bst.bfs()
print(" ")
#bst.insert(1)
#bst.insert(3)
#bst.insert(5)
print("\n\n")

bst.traversal()
bst.dfs()
print("")
print(bst.check_foldable())