import collections
from functools import cmp_to_key
def check(a, b):
    m = int(str(a) + str(b))
    n = int(str(b) + str(a))
    if (m > n):
        return -1
    elif (m < n):
        return 1
    else:
        return 0
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = sorted(nums, key = cmp_to_key (check))
        if(len(set(res)) == 1 and res[0] == 0):
            return '0'
        x = ''.join(map(str,res))
        return x