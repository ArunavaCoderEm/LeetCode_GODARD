from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        slide = SortedList(nums[0:k])
        for i in range(k, len(nums)):
            if (k % 2 == 1):
                med = slide[k // 2]
            else:
                med = (slide[k // 2] + slide[k // 2 - 1]) / 2
            res.append(float(med))
            slide.discard(nums[i - k])
            slide.add(nums[i])
        if (k % 2 == 1):
            med = slide[k // 2]
        else:
            med = (slide[k // 2] + slide[k // 2 - 1]) / 2
        res.append(float(med))
        return res


''' ANOTHER SOLN

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        i = 0
        j = 0
        res, ans = [],[]
        while(j < len(nums)):
            ans.append(nums[j])
            if(j < k - 1): j += 1
            elif(j - i == k - 1):
                arr = sorted(ans)
                dig = 0
                if(k % 2 == 0):
                    kfac = k // 2
                    dig = (arr[kfac - 1] + arr[kfac]) / 2
                else:
                    kfac = k // 2
                    dig = arr[kfac]
                res.append(dig)
                if(nums[i] in ans): ans.pop(0)
                i += 1 
                j += 1
        return res 
'''