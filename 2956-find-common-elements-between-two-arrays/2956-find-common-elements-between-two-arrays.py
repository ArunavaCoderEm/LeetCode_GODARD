class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        c1 = 0
        c2 = 0
        for i in nums1:
            if (i in nums2):
                c1 = c1 + 1
        for j in nums2:
            if (j in nums1):
                c2 = c2 + 1
        return [c1,c2]
    
        