class Solution:
    ## TWO POINTERS WITH TWO CONCEPT
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(0,len(nums) - 2):
            if(i > 0 and nums[i] == nums[i - 1]): continue
            for j in range(i+1, len(nums) - 1):
                if(j > (i + 1) and nums[j] == nums[j - 1]): continue
                k = j + 1
                l = len(nums) - 1
                while(k < l):
                    curr = nums[i] + nums[j] + nums[k] + nums[l]
                    if(curr > target): l -= 1
                    if(curr < target): k += 1
                    if(curr == target):
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        low = nums[k]
                        high = nums[l]
                        while(k < l and nums[k] == low): k += 1
                        while(k < l and nums[l] == high): l -= 1
        return res        