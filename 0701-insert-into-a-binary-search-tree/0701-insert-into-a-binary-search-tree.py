# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ptr = TreeNode(val)
        if (root == None):
            return ptr        
        if (root.val < val):
            root.right = self.insertIntoBST(root.right,val)
        else :
            root.left = self.insertIntoBST(root.left,val)
        return root
