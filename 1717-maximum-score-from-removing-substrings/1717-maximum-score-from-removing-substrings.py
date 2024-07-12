## only 22 % ??? 
## this took my 1.5+ hrs 
## I hope there's no in-built library for this !

def remstr (s, top, next, greed):

    stk = []
    res = 0

    for i in s:
        if (len(stk) and stk[-1] == top and i == next):
            stk.pop()
            res += greed
        else :
            stk.append(i)
    
    ans = ''.join(stk)
    
    return [ans, res]

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        if (not len(s)): return 0
        if (x == 0 and y == 0): return 0
        
        # if my greed is x 
        if (x > y) :
            pt1 = remstr(s, 'a', 'b', x)[1]
            s = remstr(s, 'a', 'b', x)[0]
            pt2 = remstr(s, 'b', 'a', y)[1]
            s = remstr(s, 'b', 'a', y)[0]
            
        # if not   
        elif (y > x) :
            pt1 = remstr(s, 'b', 'a', y)[1]
            s = remstr(s, 'b', 'a', y)[0]
            pt2 = remstr(s, 'a', 'b', x)[1]
            s = remstr(s, 'a', 'b', x)[0]
        
        return pt1 + pt2