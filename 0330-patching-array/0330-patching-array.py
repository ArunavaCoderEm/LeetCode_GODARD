class Solution:
    ## took my whole eve almost but was easyy 
    ## 60 % ??? there can't be a better approach IG !!
    def minPatches(self, nums: List[int], n: int) -> int:
        count, res, ind = 1, 0, 0
        while(count <= n):
            if(ind < len(nums) and nums[ind] <= count):
                count += nums[ind]
                ind += 1
            else:
                count += count
                res += 1
        return res