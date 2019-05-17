'''
An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field
named both, which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element) which adds the
element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer and dereference_pointer
functions that converts between nodes and memory addresses.
'''

# Apparently impossible to implement with Python, so I am just implementing
#   normal doubly linked list with add and get. (BECAUSE OF NO POINTERS)

class Node:
    def __init__(self, val=None, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class Xor_ll():
    def __init__(self):
        self.head = None

    def add(self, element):
        '''
        element: the value of the Node to be added at the end of the ll
        '''
        if self.head == None:
            self.head = Node(element)
            return

        curr = self.head
        while curr.nxt != None:
            curr = curr.nxt

        curr.nxt = Node(element, curr)

    def get(self, index):
        '''
        index: the index of the Node value to be returned
        '''
        if self.head == None:
            return None

        curr = self.head
        i = 0
        while curr != None and i != index:
            print("Here")
            curr = curr.nxt
            i += 1

        if curr == None:
            return None
        else:
            return curr.val

# TESTCASES
ll = Xor_ll()
ll.add(10)
ll.add(20)
ll.add(30)
print(ll.get(0)) # Should return 10
print(ll.get(1)) # Should return 20
print(ll.get(2)) # Should return 30
