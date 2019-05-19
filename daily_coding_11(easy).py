'''
Given two singly linked lists that intersect at some point,
find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
return the node with value 8.

In this example, assume nodes with the same value are the exact
same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists)
and constant space.
'''

class Node:
    def __init__(self, val = None, nxt = None):
        self.val = val
        self.nxt = nxt

class LL:
    def __init__(self):
        self.head = None


def intersect_node(A, B):

    if A.head == None or B.head == None:
        return None

    curra = A.head
    currb = B.head

    while curra != None and currb != None:
        if curra == currb:
            return curra.val

        curra = curra.nxt
        currb = currb.nxt

    return None


#TESTCASE:

# we are assuming the nodes with same value are same object
node8 = Node(8, Node(10)) 
    
A = LL()
A.head = Node(3, Node(7, node8))

B = LL()
B.head = Node(99, Node(1, node8))

print(intersect_node(A, B)) # Should be 8
