# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def rightRotate(lists, num):
    output_list = []
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])

    for item in range(0, len(lists) - num):
        output_list.append(lists[item])
 
    return output_list    

class Solution:  
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (head == None):
            return None
        res = []
        p,q = head,head
        while (p != None): 
            res.append(p.val)
            p = p.next
        d = k % len(res)
        newres = rightRotate(res,d)
            
        j = 0
        while (q != None and j < len(newres)):
            q.val = newres[j]
            j += 1
            q = q.next
        return head