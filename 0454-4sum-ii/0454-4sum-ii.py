class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        rem = defaultdict(int)
        # first two list for the sums
        for i in nums1:
            for j in nums2:
                rem[i + j] += 1 
        # these two for if previous sum complement present here or not
        for k in nums3:
            for l in nums4:
                res += rem[-k-l]
        return res