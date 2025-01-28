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


def zad184(p,q):
    rem = 0
    head = Node(None)
    guard = head
    while p and q:
        sume = p.val+q.val+rem
        if sume>=10:
            rem = sume//10
            sume %= 10
        head.next = Node(sume)
        head = head.next
        p = p.next
        q = q.next
    while p:
        sume = p.val+rem
        if sume>=10:
            rem = sume//10
            sume %= 10
        head.next = Node(sume)
        head = head.next
        p = p.next
    while q:
        sume = q.val+rem
        if sume>=10:
            rem = sume//10
            sume %= 10
        head.next = Node(sume)
        head = head.next
        q = q.next
    if rem:
        head.next = Node(rem)
    return guard.next
    

c1 = Node(9)
b1 = Node(9,c1)
a1 = Node(9,b1)

d2 = Node(9)
c2 = Node(9,d2)
b2 = Node(9,c2)
a2 = Node(9,b2)

new_1 = reverse_linked_list(a1)
new_2 = reverse_linked_list(a2)

head = zad184(new_1,new_2)

new_head = reverse_linked_list(head)

while new_head:
    print(new_head.val)
    new_head = new_head.next
