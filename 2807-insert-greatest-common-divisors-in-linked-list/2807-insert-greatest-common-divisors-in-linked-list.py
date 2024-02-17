# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def appendll(head, new_data):
   new_node = ListNode(new_data)
   if head is None:
        head = new_node
        return
   last = head
   while (last.next):
       last = last.next
   last.next =  new_node
   return head
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        res = []
        while(p != None):
            res.append(p.val)
            p = p.next
        new = []
        i = 0
        if (len(res) == 1): new = res
        while(i < len(res)-1):
            if(i == 0):
                new.append(res[i])
            new.append(math.gcd(res[i],res[i+1]))
            new.append(res[i+1])
            i += 1   
        q = ListNode(new[0])
        j = 1
        while(j < len(new)):
            q = appendll(q,new[j])
            j += 1
        return q