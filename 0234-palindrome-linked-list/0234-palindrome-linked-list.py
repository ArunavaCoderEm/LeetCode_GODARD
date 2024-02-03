# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res,p = [],head
        while(p != None):
            res.append(str(p.val))
            p = p.next
        x = ''.join(res)
        return x == x[::-1]