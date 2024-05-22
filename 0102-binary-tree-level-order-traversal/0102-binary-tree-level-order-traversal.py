# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root): # == BFS of a graph without cycles
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
        return res