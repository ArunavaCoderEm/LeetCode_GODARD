class Solution:
    def reverseVowels(self, s: str) -> str:
        
        i = 0
        j = len(s) - 1

        s = list(s)
        
        vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        while (i < j):
            if (s[i] in vow and s[j] in vow):
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
    
            elif (s[i] in vow and s[j] not in vow):
                j -= 1

            elif (s[j] in vow and s[i] not in vow):
                i += 1

            
            elif (s[i] not in vow and s[j] not in vow):
                i += 1
                j -= 1
        
        res = "".join(s)
        
        return res