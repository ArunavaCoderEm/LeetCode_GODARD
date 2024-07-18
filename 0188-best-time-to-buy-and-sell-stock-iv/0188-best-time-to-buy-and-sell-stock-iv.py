import numpy as np
from typing import List



class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
  
        def checkprofit(idx, allowbuy, dyp, lt, lim):
            
            if (idx == len(prices)): return 0
            
            if (lt >= lim): return 0
            
            if (dyp[idx][allowbuy][lt] != -1): return dyp[idx][allowbuy][lt]

            if (allowbuy):
                profit = max(-prices[idx] + checkprofit(idx + 1, 0, dyp, lt, lim), checkprofit(idx + 1, 1, dyp, lt, lim))
            else:
                profit = max(prices[idx] + checkprofit(idx + 1, 1, dyp, lt + 1, lim), checkprofit(idx + 1, 0, dyp, lt, lim))
    
            dyp[idx][allowbuy][lt] = profit

            return profit 
        
        n = len(prices)
        
        dimensions = (n, 2, k+1) 

        dyp = np.full(dimensions, -1)

        resprof = checkprofit(0, 1, dyp, 0, k)
        
        return resprof