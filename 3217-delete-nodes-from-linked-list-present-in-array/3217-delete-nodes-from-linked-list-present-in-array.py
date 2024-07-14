# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:  

    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums_set = set(nums)
        
        print(nums_set)
        
        if (not head): return None
        
        
        while (head.val in nums_set):
            head = head.next
        
        temp = head

        while (temp.next != None):
            
            if (temp.next.val in nums_set):
                temp.next = temp.next.next
            else:
                temp = temp.next
                
        return head

# Another approach
'''
def appendll (head, new_data):

        new_node = ListNode(new_data)

        if head is None:
            head = new_node
            return
        last = head
        while (last.next):
            last = last.next
 
        last.next = new_node

        return head
    
    
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums_set = set(nums)
        
        print(nums_set)
        
        rethead = ListNode(None)
        
        if (not head): return None
        
        while (head != None):
            if (head.val not in nums_set):
                print("hi")
                rethead = appendll(rethead, head.val)
                print(head.val)
            head = head.next
                
        return rethead.next
'''