class Solution:
    def romanToInt(self, s: str) -> int:
        
        romhash = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        rom_to_dig = 0
        i = 0
    
        while (i < len(s)):
            
            
            # remember this and works from left to right
            # so rohash and i < len(s) - 1 gives you index error
            # but this code first check index then move is fine
            # this took 20 mins for me to figure out !!!!!
            
            if (i < len(s) - 1 and romhash[s[i]] < romhash[s[i+1]]):
                res = romhash[s[i + 1]] - romhash[s[i]]
                rom_to_dig += res
                i += 2

            else :
                res = romhash[s[i]]
                rom_to_dig += res
                i += 1

        return rom_to_dig