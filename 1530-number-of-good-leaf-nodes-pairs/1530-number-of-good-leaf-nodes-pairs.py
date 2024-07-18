# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# kind of ver complicated !! 

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        totalcount = 0

        def dfs_dist_calc(temproot: TreeNode):
            
            if (not temproot): return [0]*(distance + 1)
            
            if (not temproot.left and not temproot.right):
                res = [0]*(distance + 1)
                res[1] = 1
                return res

            left_dist_cnt = dfs_dist_calc(temproot.left)
            right_dist_cnt = dfs_dist_calc(temproot.right)

            for i in range (1, len(left_dist_cnt)):
                for j in range (1, len(right_dist_cnt)):
                    if (i + j <= distance):
                        nonlocal totalcount
                        totalcount += (left_dist_cnt[i] * right_dist_cnt[j])
            
            curr_store = [0] * (distance + 1)
            for k in range (1, distance):
                curr_store[k+1] = (left_dist_cnt[k] + right_dist_cnt[k])
            
            return curr_store

        dfs_dist_calc(root)
        return totalcount