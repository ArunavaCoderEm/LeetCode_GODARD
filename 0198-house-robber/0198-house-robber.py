class Solution:
    ## I GUESS EASIEST SOLUTION YOU'LL GET
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 = 0,0
        i = 0
        while(i < len(nums)):
            Rob1 = rob2 + nums[i] 
            Rob2 = max(rob2,rob1)
            rob1,rob2 = Rob1,Rob2
            i += 1

        return max(rob1,rob2)