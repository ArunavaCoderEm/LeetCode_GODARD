class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() 
        res = nums[0] + nums[1] + nums[2]
        for val in range(0,len(nums)-2):
            i = val + 1
            j = len(nums) - 1
            while(i < j):
                summ = nums[val] + nums[i] + nums[j] 
                if(summ == target): return summ 
                if(abs(target - res) > abs(target - summ)): res = summ
                if(summ > target): j -= 1
                if(nums[val] + nums[i] + nums[j] < target): i += 1
        return res      