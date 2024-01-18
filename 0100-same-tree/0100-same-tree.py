# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preorder(root,res):
            if(root == None):
                res.append(None)
                return
            res.append(root.val)
            preorder(root.left,res)
            preorder(root.right,res)
        x,y = [],[]
        preorder(p,x)
        preorder(q,y)
        return x == y