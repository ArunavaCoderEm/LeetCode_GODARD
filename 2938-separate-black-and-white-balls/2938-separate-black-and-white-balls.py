# ezzz
# #8 from pending
# all the black count faced from L to R is the no. of swaps 
# so it's better not to check after swapping values

class Solution:
    def minimumSteps(self, s: str) -> int:
        black_count = 0
        swaps = 0

        for char in s:
            if char == '1':
                black_count += 1
            elif char == '0':
                swaps += black_count

        return swaps
