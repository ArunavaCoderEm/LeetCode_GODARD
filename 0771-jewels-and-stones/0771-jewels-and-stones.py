class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in list(set(jewels)):
            if (i in stones): count += stones.count(i)
        return count