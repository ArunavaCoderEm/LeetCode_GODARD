class Solution:
    # THANKS TO PYTHON3 :-)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[-1][0]