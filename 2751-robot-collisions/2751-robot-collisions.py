## You were not even that hard still you almost took my life
## I was substracting both the healths where I should have substracted just 1 
## that costed me an hour !!!!!

def givepos(posarr):
    return posarr[0]

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        stk = []

        robotstats = []

        for i in range(len(positions)):
            ans = [positions[i], healths[i], directions[i], i]      
            robotstats.append(ans)
            
        print(robotstats)
        
        robotstatssort = sorted(robotstats, key = givepos)

        for j in robotstatssort:

            if (j[2] == 'L'):

                while (len(stk) and stk[-1][2] == 'R' and stk[-1][1] < j[1]):
                    stk.pop()
                    j[1] = j[1] - 1
                    
                if (not len(stk) or stk[-1][2] == 'L'):
                    stk.append(j)
                    
                elif (len(stk) and stk[-1][1] == j[1]):
                    stk.pop()
                    
                elif (len(stk) and stk[-1][1] > j[1]):
                    stk[-1][1] -= 1
                    
            else :
                stk.append(j)
                
        retres = []
        
        for k in stk:
            retres.append(k[1])
            
        idx_health = {k[3]: k[1] for k in stk}
        
        sorted_indices = sorted(idx_health.keys())
        retres = [idx_health[idx] for idx in sorted_indices]
        
        return retres