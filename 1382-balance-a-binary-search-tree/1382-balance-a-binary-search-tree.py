# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Kind of AVL tree concept

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        # hint 1

        def inorder(root: TreeNode, res: list) -> list:
            if (root is not None):
                inorder(root.left, res)
                res.append(root.val)
                inorder(root.right, res)

        res = []
        inorder(root, res)

        # hint 2

        def avlBST(ans: list) -> TreeNode : 
            if (not ans): return None
            mid = len(ans) // 2
            node = TreeNode(ans[mid])
            node.left = avlBST(ans[:mid])
            node.right = avlBST(ans[mid + 1:])
            return node

        if(not res): return None
        return avlBST(res)