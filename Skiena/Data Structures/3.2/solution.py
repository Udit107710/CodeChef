class Node(object):
    def __init__(self, val):
        super().__init__()
        self.val = val
        self.next = None

class LinkedList(object):
    def __init__(self, val):
        super().__init__()
        self.head = Node(val)
        self.tail = self.head
    
    def add_node(self, val):
        head = self.head
        while head.next is not None:
            head = head.next
        head.next = Node(val)

    def print(self):
        head = self.head
        while head is not None:
            print(head.val, '->')
            head = head.next
        print('tail')

    def reverse(self):
        current_head = self.head
        head = self.head

        while current_head is not None:
            temp = current_head
            current_head = head.next
            t_next = current_head.next
            head.next = t_next
            current_head.next = temp

            if head.next is None:
                self.head = current_head
                break

ll = LinkedList("A")
ll.add_node("B")
ll.add_node("C")
ll.add_node("D")

ll.print()
ll.reverse()
ll.print()