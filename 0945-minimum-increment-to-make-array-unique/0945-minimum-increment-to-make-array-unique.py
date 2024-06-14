class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # ez sort and check current elements
        ## BRUV WHEN WILL I GET SOME BEATS ABOVE 70 ?????
        nums.sort()
        c = 0
        for i in range(len(nums) - 1):
            if(nums[i+1] <= nums[i]):
                c += nums[i] - nums[i+1] + 1
                nums[i+1] = nums[i] + 1
        return c