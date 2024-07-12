# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 7 from pending

def search(root, val):
    if(root == None): return None
    if(root.val == val): return root
    elif(val < root.val): 
        return search(root.left, val)
    else:
        return search(root.right, val)

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        flag = search(root, val)
        if(not flag):
            return None
        return flag

