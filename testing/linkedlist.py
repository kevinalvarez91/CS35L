# Making a linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # Defining the arrow

if __name__ = '__main__':
    root = Node(0)
    curr = root
    for num in range(1, 10):
        curr.next = Node(num)
        curr = curr.next

#traversing
    curr = root
    while curr is not None:
        print(curr.value)
        curr = curr.next
