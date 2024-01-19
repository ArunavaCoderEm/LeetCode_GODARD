class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        temp = []
        ress = list(nums[0:n])
        res = list(nums[n:len(nums)])
        i = 0
        while (i < len(res)):
            temp.append(ress[i])
            temp.append(res[i])
            i += 1
        return temp