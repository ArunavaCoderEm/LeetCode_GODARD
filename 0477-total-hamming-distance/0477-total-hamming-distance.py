## Ezz bit manipulation 
## xor is 1 when between different bits 
## that's why the differbits function acts like that

def differbits(m, n):
    difbit = m ^ n
    difbitbin = bin(difbit)[2:]
    res = difbitbin.count('1')
    return res
    
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        totalhamdist = 0
        for i in range(32): 
            count = 0
            flag = (1 << i)
            for num in nums:
                if (num & flag):
                    count += 1
            totalhamdist += count * (len(nums) - count)
        return totalhamdist