class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next=next

def zad197(p):
    if not p:
        return p
    slow = p
    fast = p
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cnt = 0
            while True:
                slow = slow.next
                cnt+=1
                if slow == fast:
                    return cnt
    return 0


g = Node(7)
f = Node(6,g)
e = Node(5,f)
d = Node(4,e)
c = Node(3,d)
b = Node(2,c)
a = Node(1,b)
g.next = c

print(zad197(a))