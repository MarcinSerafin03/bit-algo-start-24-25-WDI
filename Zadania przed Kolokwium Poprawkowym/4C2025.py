class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

    def __str__(self):    
        return str(self.val) + (" -> " + str(self.next) if self.next else "")
def fix(p):
    head = p
    prev = None
    prev_start = None
    start = None
    end = None
    flag = False
    while head:
        prev = head
        head = head.next
        if head and head.val<prev.val:
            start = head
            prev_start = prev
        if prev_start and head and not flag and prev_start.val<head.val:
            flag = True
            end = prev
            prev_start.next = head
        if prev_start and not flag and not head:
            flag = True
            end = prev
            prev_start.next = head
    head = p
    prev = None
    while head:
        if not prev and head.val>end.val:
            end.next=head
            p = start
        prev = head
        head = head.next
        if prev.val<start.val and head.val>end.val:
            prev.next=start
            end.next=head
    
    return p

T = [2,3,23,29,5,7,11,13,17,19,31,37,41,43,47,53]
T1 = [17,19,23,29,31,37,41,2,3,5,7,11,13,43,47,53]
T2 = [2,3,23,29,31,37,41,43,47,53,5,7,11,13,17,19]


def list_to_linked_list(arr):
    """    Konwertuje listę na listę jednokierunkową i zwraca jej pierwszy element.    """    
    if not arr:        
        return None    
    head = Node(arr[0])   
    current = head   
    for val in arr[1:]:        
        current.next = Node(val)        
        current = current.next    
    return head

p = fix(list_to_linked_list(T2))
print(p)

