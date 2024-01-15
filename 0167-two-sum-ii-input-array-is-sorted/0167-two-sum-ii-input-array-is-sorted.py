class Solution:
    def twoSum(self,numbers, target):
        res = []
        for i in range (len(numbers)):
            complement = target - numbers[i]
            if (complement not in numbers):
                continue
            j = numbers.index(complement)
            if (i != j and complement in numbers):
                res.append(i+1)
                res.append(j+1)
                res.sort()
                return res 