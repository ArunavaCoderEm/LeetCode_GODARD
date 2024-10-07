class Solution:
    def maxPointsInsideSquare(self, points, s):
        n = len(points)
        for i in range(0, n):
            points[i][0] = abs(points[i][0])
            points[i][1] = abs(points[i][1])

        start, end, ans = 0, 696969696969696969, 0
        while (start <= end):
            mid = (start + (end - start) // 2) ## /2 gives float "how can i forget !!"
            val = True
            d = {}

            for j in range(0, n):
                if (points[j][0] <= mid and points[j][1] <= mid):
                    d[s[j]] = d.get(s[j], 0) + 1
            for key, value in d.items():
                if (value > 1):
                    val = False
                    break
            if (val):
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        count = 0
        for k in range(0, n):
            if (points[k][0] <= ans and points[k][1] <= ans):
                count += 1
        return count
