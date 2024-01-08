class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1
        while (low <= high):
            mid = (low + high) // 2
            if (nums[mid] > target):
                high = mid - 1
            elif (nums[mid] < target):
                low = mid + 1
            else :
                return mid
        return low
            
        

 #THIS CAN BE ONE SOLUTION
#  class Solution(object):
#     def searchInsert(self, nums, target):
#         nums.append(target)
#         nums.sort()
#         return nums.index(target)          