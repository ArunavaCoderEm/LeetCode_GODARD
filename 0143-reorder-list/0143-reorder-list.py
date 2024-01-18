# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p,q,res = head,head,[]
        while(p != None):
            res.append(p)
            p = p.next
        i = 0
        half = len(res)//2
        while i < half:
            temp = res[i].next
            res[i].next = res[~i]
            res[~i].next = temp ## BITWISE EZZ
            i += 1
        res[half].next = None ## CONNECT End (I forgot to connect and it took me 15 mins to think of this little fix) 
        return head
            