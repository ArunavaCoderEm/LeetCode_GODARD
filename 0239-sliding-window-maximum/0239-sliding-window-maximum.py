# class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # i,j,res = 0,k,[]
        # while(i < len(nums) - k + 1):
        #     res.append(max(nums[i:j]))
        #     i += 1
        #     j += 1
        # return res
## any answer
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        res = []
        ans = []
        for j in range(len(nums)):
            while (len(ans) > 0 and nums[j] > ans[len(ans)-1]):
                ans.pop()
            ans.append(nums[j])
            if ((j-i+1) == k):
                res.append(ans[0])
                if (ans[0] == nums[i]):
                    ans.remove(ans[0])
                i += 1
        return res