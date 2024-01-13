class Solution(object):
    def merge(self, nums1, m, nums2, n):
        c = []
        for i in range (m):
            c.append(nums1[i])
        for j in range (n):
            c.append(nums2[j])
        c.sort()
        for k in range (len(c)):
            nums1[k] = c[k]
            
            