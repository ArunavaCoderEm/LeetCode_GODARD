# Easiest medium I guess

from collections import Counter
from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        if (k < 0): return 0
        
        c = Counter(nums)
        
        pairs = 0
        KchkLst = c.keys()
        VchkLst = c.values()
        
        
        if (k == 0):
            for count in VchkLst:
                if (count > 1):
                    pairs += 1
        
        else:
            for i in KchkLst:
                if ((i + k) in KchkLst): pairs += 1
            
        return pairs