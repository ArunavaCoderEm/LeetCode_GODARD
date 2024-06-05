def dfs(rooms, n, vis):
    if(n in vis): return
    vis.add(n)
    for i in rooms[n]:
        dfs(rooms,i,vis)

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis = set()
        dfs(rooms,0,vis)
        res = (len(vis) == len(rooms))
        return res