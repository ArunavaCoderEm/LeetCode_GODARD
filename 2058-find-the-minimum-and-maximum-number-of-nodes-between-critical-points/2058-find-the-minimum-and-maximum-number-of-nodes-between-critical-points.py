# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## damn I'm becoming good in LC
## Today i'll try to complete all my pendings ! 1 complete

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
	    
        pos = 2
        criticalpts = []
        
        if (head is None or head.next is None or head.next.next is None):
            return [-1, -1]

        start = head
        mid = start.next
        end = mid.next
        
        while (end):
            if(mid.val > start.val and mid.val > end.val): 
                criticalpts.append(pos)
            if(mid.val < start.val and mid.val < end.val): 
                criticalpts.append(pos)
                
            start = mid
            mid = start.next
            end = mid.next
            pos += 1
        
        if(len(criticalpts) == 2): 
            maxdiff = abs(criticalpts[0] - criticalpts[1])
            mindiff = abs(criticalpts[0] - criticalpts[1]) 
            return [mindiff, maxdiff]
        
        print(criticalpts)

        if(len(criticalpts) < 2): return [-1,-1]

        maxdiff = abs(criticalpts[0] - criticalpts[-1])
        mindiff = float("inf") 
        
        for i in range(0,len(criticalpts) - 1):
            mindiff = min(mindiff, abs(criticalpts[i] - criticalpts[i + 1]))
        
        return [mindiff, maxdiff]

        