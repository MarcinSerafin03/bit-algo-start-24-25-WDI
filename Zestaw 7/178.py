class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next=next


def reverse_linked_list(p):
    prev = None
    head = p
    while head:
        next_node = head.next
        head.next=prev
        prev = head
        head = next_node
    
    return prev 

c = Node(3)
b = Node(2,c)
a = Node(1,b)

reverse_linked_list(a)

while c:
    print(c.val)
    c = c.next

