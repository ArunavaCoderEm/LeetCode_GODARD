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
        p,res = head,[]
        if(head == None):
            return head
        while(p != None):
            res.append(p.val)
            p = p.next
        x = [i for i in res if res.count(i) <= 1]
        if (len(x) == 0):
            return None
        q,j = head,1
        headr = ListNode(x[0])
        headr.next = None
        while (j < len(x)):
            headr = appendl(headr,x[j])
            j += 1
        return headr