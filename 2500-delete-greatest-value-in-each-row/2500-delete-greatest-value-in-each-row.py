class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = []
        row = len(grid)
        while (len(grid[0]) != 0):
            res = []
            for i in range (row):
                res.append(max(grid[i]))
                grid[i].remove(max(grid[i]))
            ans.append(max(res))
        return sum(ans)