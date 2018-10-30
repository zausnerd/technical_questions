class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            cursor = self.head
            while cursor.next is not None:
                cursor = cursor.next
            cursor.next = Node(value)
    def print_values(self):
        cursor = self.head
        while cursor is not None:
            print(cursor.value)
            cursor = cursor.next

def kth_last_element(node, k):
    kth_node = node
    cursor_node = node
    for	i in range(0, k + 1):
        kth_node = kth_node.next
    while kth_node is not None:
        kth_node = kth_node.next
        cursor_node = cursor_node.next
    print(cursor_node.value)
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)
kth_last_element(ll.head, 2)
