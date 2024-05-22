# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## with the same logic if you use dequeue library then use pop it'll do it in O(1)
## but with this pop(0) it's done in O(n)
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root): return []
        Q = [root]
        res = []
        while(Q):
            n = len(Q)
            ans = []
            for i in range (n):
                k = Q.pop(0)
                if(k): 
                    ans.append(k.val)
                    if(k.left): Q.append(k.left)
                    if(k.right): Q.append(k.right)
            if(k): res.append(ans)
        res.reverse()       
        return res        