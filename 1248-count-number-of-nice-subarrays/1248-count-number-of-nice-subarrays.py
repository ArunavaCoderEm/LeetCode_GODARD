## took time a lot but damn im good with recs

class Solution:
    def odd_count(self, sublist: List[int]) -> int:
        return sum(1 for x in sublist if x % 2 != 0)
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k: int) -> int:
            count = 0
            left = 0
            result = 0
            for right in range(len(nums)):
                if (nums[right] % 2 != 0):
                    count += 1
                while (count > k):
                    if (nums[left] % 2 != 0):
                        count -= 1
                    left += 1
                result += right - left + 1
            return result
        return atMost(k) - atMost(k - 1)
