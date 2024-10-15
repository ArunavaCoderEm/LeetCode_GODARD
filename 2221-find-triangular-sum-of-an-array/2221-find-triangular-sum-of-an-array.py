# good LC day

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        temp = nums

        while (len(temp) > 1):

            sumtemp = []

            for i in range(0, len(temp) - 1):

                summ = (temp[i] + temp[i+1]) % 10
                sumtemp.append(summ)

            temp = sumtemp

        return temp[0]
