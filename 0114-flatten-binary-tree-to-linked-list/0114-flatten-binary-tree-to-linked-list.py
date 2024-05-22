# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorder(root, res):
    if(root != None):
        res.append(root.val)
        preorder(root.left, res)
        preorder(root.right, res)

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        res = []
        ans = root
        if(not root): return res
        preorder(root,res)
        for i in range(1,len(res)):
            ans.left = None
            ans.right = TreeNode(res[i])
            ans = ans.right