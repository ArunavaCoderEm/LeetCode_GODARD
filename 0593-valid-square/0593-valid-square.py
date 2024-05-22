def dis(x1,x2):
    d1 = abs(x1[0] - x2[0])
    d2 = abs(x1[1] - x2[1])
    return (d1**2 + d2**2)
# thnx yt
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        res = [
            dis(p1,p2),
            dis(p2,p3),
            dis(p1,p3),
            dis(p3,p4),
            dis(p1,p4),
            dis(p2,p4)
        ]
        res.sort()
        return (res[0] > 0 and res[0] == res[1] and res[1] == res[2] and
                res[2] == res[3] and res[4] == res[5] and
                res[4] == 2 * res[0])