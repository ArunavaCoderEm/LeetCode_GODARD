class Solution:
    ## easiest greedy approacch
    ## if ast > pla return false immd
    ## sort asc and add mass if not
    ## okay not that much beats so may not be the best !!
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for i in range(len(asteroids)):
            if(asteroids[i] <= mass):
                mass += asteroids[i]
            else : return False
        return True