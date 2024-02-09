# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import numpy as np

def swapnode(arr,k):
    i,j,count = 0,k,0
    while(count <= len(arr) and len(arr[i:]) > k-1):
        arr[i:j] = np.flip(arr[i:j], axis=0)
        i,j = i+k,j+k
        count += k
    return arr

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p,res,q = head,[],head
        while(p != None):
            res.append(p.val)
            p = p.next
        ress = swapnode(res,k)
        for i in ress:
            q.val = i
            q = q.next
        return head