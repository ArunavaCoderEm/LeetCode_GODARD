class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        # hint 2
        minn = min(enemyEnergies)
        # hint 3
        res = currentEnergy + sum(enemyEnergies)
        # hint 4
        if(currentEnergy < minn): return 0
        # hint 1
        res -= minn
        ans = res // minn
        return ans  