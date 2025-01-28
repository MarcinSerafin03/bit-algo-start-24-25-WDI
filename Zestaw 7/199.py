class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next=next

def zad198(p):
    if not p:
        return p
    slow = p
    fast = p
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow2 = p
            prev = p
            slow2 = slow2.next
            slow = slow.next
            while True:
                if slow==slow2:
                    return prev
                prev = slow2
                slow = slow.next
                slow2 = slow2.next



g = Node(7)
f = Node(6,g)
e = Node(5,f)
d = Node(4,e)
c = Node(3,d)
b = Node(2,c)
a = Node(1,b)
g.next = c

print(zad198(a))
