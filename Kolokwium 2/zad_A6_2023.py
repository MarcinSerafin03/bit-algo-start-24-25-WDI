from math import log10
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next=next


def insert(p,n):
    head = p
    beginning = n//(10**(int(log10(n))))
    ending = n%10
    first = None
    last = None
    flag = True
    while flag:
        first_digit = head.val//(10**(int(log10(head.val))))
        if first_digit == beginning:
            cnt = 1
            first = head
            head = head.next
            while flag:
                last_digit = head.val%10
                if last_digit == ending:
                    last = head
                    flag = False
                head = head.next
                cnt+=1
                if not last and head == first:
                    return 0
        head = head.next
        if not first and head == p:
            return 0
    head = p
    prev = p
    head = head.next
    while True:
        if head == first:
            prev.next = Node(n,last.next)
            return cnt
        head = head.next




def list_to_ll(List: list):
    head = current = Node(List[0])
    for i in range(1, len(List)):
        new = Node(List[i])
        current.next = new
        current = new
    current.next = head
    return head


T = [2023, 31 ,17 ,703, 37, 707, 72,29,902]
p = list_to_ll(T)
print(insert(p,99))

