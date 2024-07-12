# 9 of pending

# with const lookup and O(n) 7 % ????

def get_vowels(s) -> int:
    # for almost const lookup
    vow_set = {'a', 'e', 'i', 'o', 'u'}
    if(s in vow_set): return True
    return False
    

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxvow = float("-inf")
        curr = 0
        for i in range(k):
            if (get_vowels(s[i])):
                curr += 1
        maxvow = curr
        for i in range(k, len(s)):
            if (get_vowels(s[i - k])):
                curr -= 1
            if (get_vowels(s[i])):
                curr += 1    
            maxvow = max(maxvow, curr)
        
        return maxvow
