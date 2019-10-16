#Question: https://leetcode.com/problems/my-calendar-i/

class Node:
    def __init__(self, start, end):
        self.e = end
        self.s = start
        self.left = None
        self.right = None
    
class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root:
            return self.insert(start, end, self.root)
        
        self.root = Node(start, end)
        return True
       
    
    def insert(self, start, end, node):
        if start >= node.e:
            if node.right:
                return self.insert(start, end, node.right)
            else:
                node.right = Node(start, end)
                return True
        elif end <= node.s:
            if node.left:
                return self.insert(start, end, node.left)
            else:
                node.left = Node(start, end)
                return True
        else:
            return False
        