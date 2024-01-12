class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        temp = sorted(heights)
        for i in range(len(heights)):
            if(temp[i] != heights[i]):
                count += 1
        return count