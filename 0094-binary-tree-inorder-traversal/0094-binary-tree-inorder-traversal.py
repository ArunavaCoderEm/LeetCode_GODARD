# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        c = []
        def inorderaAg(root):
            if (not root):
                return
            inorderaAg(root.left)
            c.append(root.val)
            inorderaAg(root.right)
        inorderaAg(root)
        return c
        