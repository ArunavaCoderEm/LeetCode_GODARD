class Solution:
    ## the easiest approach maybe
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if(nums == sorted(nums)): return  0
        count = 0
        end = -1
        res = sorted(nums)
        for i in range(0,len(nums)):
            if(res[i] != nums[i] and count == 0):
                st = i
                count += 1
            elif(res[i] != nums[i] and count > 0):
                end = max(i,end) 
        return (end - st + 1)
