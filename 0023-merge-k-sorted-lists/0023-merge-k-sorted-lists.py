# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def appendll(head,new_data):
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        res1 = []
        if(len(lists) == 0):
            return None
        for i in range (len(lists)):
            p = lists[i]
            if((lists[i]) == None):
                res1.append(1)
            while(p != None):
                res.append(p.val)
                p = p.next
        if(len(res1) == len(lists)):
            return None
        res.sort()
        head = ListNode()
        if(len(res) ==  0): 
            head == None
            return head
        head.val = res[0]
        head.next = None
        j = 1
        while(j != len(res)):
            head = appendll(head,res[j])
            j += 1
        return head