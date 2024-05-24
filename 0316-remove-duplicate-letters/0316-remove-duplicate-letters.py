class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        vis = [] ## basic brute force sorry it's 2AM
        for i in range(len(s)):
            if(s[i] not in vis):
                chidx = len(vis) - 1
                while(chidx >= 0 and vis[chidx] > s[i]):
                    if (not(vis[chidx] in s[i+1:])): break
                    vis.pop()
                    chidx -= 1
                vis.append(s[i])
        return "".join(vis)