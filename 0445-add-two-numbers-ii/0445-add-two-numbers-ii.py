# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1,sum2 = 0,0
        p,q = l1,l2
        while(p!=None):
            sum1 = (10*sum1)+p.val
            p=p.next
        while(q!=None):
            sum2 = (10*sum2)+q.val
            q=q.next
        sum3 = str(sum1+sum2)
        j = 1
        head = ListNode()
        head.val = int(sum3[0])
        head.next = None
        while(j<len(sum3)):
            new_node = ListNode(int(sum3[j]))
            last = head
            new_node.next = None
            if head is None:
                return new_node
            while last.next is not None:
                last = last.next
            last.next = new_node
            j+=1
        return head