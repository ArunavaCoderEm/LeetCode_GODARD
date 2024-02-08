# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def appendl(head,new_data):
   new_node = ListNode(new_data)
   if head is None:
        head = new_node
        return
   last = head
   while (last.next):
       last = last.next
   last.next =  new_node
   return head

class Solution:  
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        p,q = head,head
        res = []
        while (p != None):
            res.append(p.val)
            p = p.next
        ress = [i for i in res if (i != val)]
        if(len(ress) == 0): return None
        heady = ListNode(ress[0])
        for j in range(1,len(ress)):
            heady = appendl(heady,ress[j])
        return heady