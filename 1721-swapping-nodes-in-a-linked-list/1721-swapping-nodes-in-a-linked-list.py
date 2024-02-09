# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def swapnodes(arr,k):
    temp = arr[k-1]
    arr[k-1] = arr[len(arr)-k] 
    arr[len(arr)-k] = temp
    return arr
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p,q,res,ress = head,head,[],[]
        while(p != None):
            res.append(p.val)
            p = p.next
        ress = swapnodes(res,k)
        for i in ress:
            q.val = i
            q = q.next
        return head