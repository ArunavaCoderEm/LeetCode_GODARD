# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def nextGreaterElement(arr):
  n = len(arr)
  result = [0] * n
  s = []
  for i in range(n):
    while len(s) > 0 and arr[s[-1]] < arr[i]:
      result[s.pop()] = arr[i]
    s.append(i)
  return result

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        p = head
        g = []
        while(p != None):
            g.append(p.val)
            p = p.next
        ans = nextGreaterElement(g)
        return ans