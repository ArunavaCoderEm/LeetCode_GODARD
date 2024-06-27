## don't do this dirtiest solution LOLLL

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if(len(edges) == 1): return edges[0][0]
        if(len(edges) == 0): return
        m = edges[0]
        n = edges[1]
        for i in m:
            if(i == n[0]): return i
            elif(i == n[1]): return i