class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if(nums[0] + nums[1] <= nums[2]):return "none"
        if(nums[0] + nums[2] <= nums[1]):return "none"
        if(nums[2] + nums[1] <= nums[0]):return "none"
        if(nums[0] == nums[1] and nums[0] == nums[2]):
            return "equilateral"
        elif(len(set(nums)) == 2): return "isosceles"
        else: return "scalene"