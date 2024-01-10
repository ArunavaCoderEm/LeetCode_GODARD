# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        c = []
        def postorderag(root):
            if (not root):
                return 
            postorderag(root.left)
            postorderag(root.right)
            c.append(root.val)
        postorderag(root)
        return c
    