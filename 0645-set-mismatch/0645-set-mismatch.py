class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in list(set(nums)):
            if(nums.count(i) == 2):
                res.append(i)
        n = len(nums)
        summ = (n*(n+1))//2 
        summm = summ-sum(nums) + res[0]

        res.append(summm)
        return res