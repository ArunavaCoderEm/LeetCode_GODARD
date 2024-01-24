# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def appendl(head_ref, new_data):
    new_node = ListNode(new_data)
    last = head_ref
    new_node.next = None
    if head_ref is None:
        return new_node
    while last.next is not None:
        last = last.next
    last.next = new_node 
    return head_ref

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        if (head == None):
            return head
        p,q = head,head   
        while(p != None):
            res.append(p.val)
            p = p.next
        ress = (list(set(res)))
        ress.sort()
        j = 1
        headr = ListNode()
        headr.val = ress[0]
        headr.next = None
        while (j < len(ress)):
            headr = appendl(headr,ress[j])
            j += 1
        return headr