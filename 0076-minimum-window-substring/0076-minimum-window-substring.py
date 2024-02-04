# def check(p,t):
#     if (all((c in p) and t.count(c) <= p.count(c) for c in t)):
#         return True
#     else:
#         return False
# ## sliding window concept
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if(len(s) < len(t)):
#             return ""
#         if(t in s):
#             return t
#         elif(len(s) == 1 and t in s):
#             return s
#         i,j,res = 0,1,set()
#         while(i < len(s) - 1):
#             if(check(s[i:j],t) and len(s[i:j]) >= len(t)):
#                 res.add(s[i:j])
#                 j += 1     
#                 if(j > len(s) - 1 and check(s[i:j],t)):
#                     res.add(s[i:j])
#                     i += 1
#                     j = i + 1
#                 else:
#                     i += 1
#                     j = i + 1
#             else:
#                 j += 1
#             if(j > len(s)):
#                 i += 1
#                 j = i + 1
#         ress = sorted(res,key=len)
#         if(len(ress) == 0): return ""
#         return ress[0]

## Another approach

class Solution:
    def minWindow(self, s: str, t: str) -> str:       
        c = Counter(t)
        d = {}     
        count = 0
        res = float('inf'), 0, 0 ## thanks sohan for 'float('inf')'
        l, r = 0, 0
        while (r < len(s)):
            ch = s[r] 
            d[ch] = d.get(ch, 0) + 1 
            if (ch in c and d[ch] == c[ch]):
                count += 1
            while (l <= r and count == len(c)):
                last = s[l]
                if (res[0] > (r-l+1)): res = (r-l+1), l, r                                   
                d[last] -= 1
                if (last in c and d[last] < c[last]):
                    count -= 1           
                l += 1         
            r += 1  
        return "" if (res[0] == float('inf')) else (s[res[1]:res[2]+1])