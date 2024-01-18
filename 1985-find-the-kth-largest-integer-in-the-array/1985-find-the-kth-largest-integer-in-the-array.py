class Solution:
    ## EASIEST SOLUTION I GUESS
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        res = list(map(int,nums))
        res.sort()
        return str(res[-k])