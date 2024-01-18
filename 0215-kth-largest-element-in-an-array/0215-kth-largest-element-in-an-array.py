class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums = nums[0:len(nums)-k+1]
        return nums[len(nums) - 1]