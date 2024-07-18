from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def checkprofit(idx, allowbuy, dyp):
            
            if (idx == len(prices)): return 0
            
            if (dyp[idx][allowbuy] != -1): return dyp[idx][allowbuy]

            if (allowbuy):
                profit = max(-prices[idx] + checkprofit(idx + 1, 0, dyp), checkprofit(idx + 1, 1, dyp))
            else:
                profit = max(prices[idx] + checkprofit(idx + 1, 1, dyp), checkprofit(idx + 1, 0, dyp))
    
            dyp[idx][allowbuy] = profit

            return profit 
        
        n = len(prices)
        dyp = []
        for _ in range(n):
            dyp.append([-1,-1])
            
        print(dyp)

        resprof = checkprofit(0, 1, dyp)
        
        return resprof