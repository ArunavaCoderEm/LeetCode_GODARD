## Eazz two pointer approach
## dont waste TC on removing just move pointers
## then youll never see those elements again
## that's kind of equivalant of removing

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        if(not len(nums)): return 0

        nums.sort()
        ope = 0
        
        i = 0
        j = len(nums) - 1
        
        while (i < j):
            
            if (nums[i] + nums[j] < k):
                i += 1
            elif (nums[i] + nums[j] > k):
                j -= 1
            elif (nums[i] + nums[j] == k):
                ope += 1
                i += 1
                j -= 1
        
        return ope 