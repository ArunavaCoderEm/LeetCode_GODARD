# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# just traverse from bottom ie (dfs) and sum ezzz approach
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, res):
            if (node):
                res = dfs(node.right, res)
                res += node.val
                node.val = res
                res = dfs(node.left, res)
            return res
        dfs(root, 0)
        return root
