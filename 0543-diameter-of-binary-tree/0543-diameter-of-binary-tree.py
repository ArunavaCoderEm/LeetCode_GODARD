# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def inorder(root):
            nonlocal res 
            if(root == None):
                return 0
            left = inorder(root.left)
            right = inorder(root.right)
            res = max(res,(left + right))
            return 1 + max(left,right)
        inorder(root)
        return res