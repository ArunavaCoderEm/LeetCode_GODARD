class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0
        l = max(nums1)
        c = Counter(nums2)
        c1 = Counter(nums1)
        print(c)
        for i in c:
            m = 1
            u = i * k
            while(u*m <= l):
                count += c[i] * c1[u*m]
                m += 1
        return count