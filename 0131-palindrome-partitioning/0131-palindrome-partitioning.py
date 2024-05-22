def kindofdfs(s, count, ans, res):
    if (count == len(s)):
        res.append(ans)
        return
    for i in range(count, len(s)):
        if (s[count : i+1] == s[count : i+1][::-1]):
            a = ans.copy()
            a.append(s[count : i+1])
            kindofdfs(s, i+1, a, res)
##### BRO WHY ONLY 60 % ?????? I CAN'T THINK OF A BETTER ONE !!!!!!!!!
## OKAY NOW IT CAME 94% WITH SAME CODE !!! WTF
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        kindofdfs(s, 0,[],res)
        return res