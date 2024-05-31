# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    ## why this less beats ?? this is the only soln I guess !!
    def __init__(self, root: Optional[TreeNode]):
        self.l = []
        while(root):
            self.l.append(root)
            root = root.left

    def next(self) -> int:
        node = self.l.pop()
        while(node.right):
            self.l.append(node.right)
            node.right = node.right.left
        return node.val

    def hasNext(self) -> bool:    
        x = (len(self.l) == 0)
        return not x

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()