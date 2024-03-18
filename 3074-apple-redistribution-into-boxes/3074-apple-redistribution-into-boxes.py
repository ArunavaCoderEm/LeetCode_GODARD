class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        capacity.sort()
        i = len(capacity) - 1
        count = 0
        while(s > 0 and i >= 0):
            s -= capacity[i]
            i -= 1
            count += 1
        return count