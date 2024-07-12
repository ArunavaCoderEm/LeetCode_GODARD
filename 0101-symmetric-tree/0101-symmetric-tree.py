# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ezz stack implmnt
# 10 of pending

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [(root.left, root.right)]
        
        while stack:
            le, ri = stack.pop()
            
            if (not le and not ri):
                continue
            
            if (not le or not ri or le.val != ri.val):
                return False
            
            stack.append((le.left, ri.right))
            stack.append((le.right, ri.left))
        
        return True


