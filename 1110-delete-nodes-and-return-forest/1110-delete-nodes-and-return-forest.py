# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def postOrderWithDel(root: Optional[TreeNode], res: List[TreeNode], checkset: Set[int]) -> Optional[TreeNode]:
    if not root:
        return None

    root.left = postOrderWithDel(root.left, res, checkset)
    root.right = postOrderWithDel(root.right, res, checkset)

    if root.val in checkset:
        if root.left:
            res.append(root.left)
        if root.right:
            res.append(root.right)
        return None

    return root

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        res = []
        root = postOrderWithDel(root, res, to_delete_set)

        if root and root.val not in to_delete_set:
            res.append(root)

        return res