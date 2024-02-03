# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p,res = head,[]
        if(head == None): return None
        while(p != None):
            res.append(p.val)
            p = p.next
        res.reverse()
        q = head
        i = 0
        while(q != None):
            q.val = res[i]
            i += 1
            q = q.next
        return head
