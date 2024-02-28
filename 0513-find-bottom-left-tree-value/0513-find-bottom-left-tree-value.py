# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = []
        t = root
        ans.append(t)
        ## easy iterative inorder traversal
        while(len(ans) != 0):
            t = ans[0]
            ans = ans[1:]
            if(t.right != None): ans.append(t.right)
            if(t.left != None): ans.append(t.left)
        return t.val