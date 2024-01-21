# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def kthSmallest(arr, N, K):
    arr.sort()
    return arr[K-1] 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root,res):
            if (root != None):
                p = root
                inorder(p.left,res)
                res.append(p.val)
                inorder(p.right,res)
            return res
        val = []
        inorder(root,val)
        return val[k-1] 
        