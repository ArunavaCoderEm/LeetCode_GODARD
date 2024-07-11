# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# dont particularly check for conseq but 
# check each if next is not none then move forward the
# connected component of LL
## Ezz approach

# 5 of my pendings

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        # with list only it was giving 56%
        # convert to set as constant lookup
        num_set = set(nums)
        compo = 0
        
        if(len(nums) == 1): return 1
        if(head == None): return None
        if(head.next == None):
            x = head.val
            if(x in nums): return 1
            
        temp = head
        
        print(nums)
        
        while(temp != None):
            if (temp.val in num_set and (temp.next is None or temp.next.val not in num_set)):
                compo += 1
            temp = temp.next
        
        return compo