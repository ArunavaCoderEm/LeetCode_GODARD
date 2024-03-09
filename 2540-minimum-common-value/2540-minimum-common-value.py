class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        res1 = set(nums1)
        res2 = set(nums2)
        if((res1 & res2)):
            res3 = list(res1 & res2)
            res3.sort()
            return res3[0]
        else:
            return -1