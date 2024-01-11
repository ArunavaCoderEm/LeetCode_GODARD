# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        try :
            q = head.next
            p = head
            while (p != q):
                p = p.next
                q = q.next.next
            return True
        except :
            return False
        