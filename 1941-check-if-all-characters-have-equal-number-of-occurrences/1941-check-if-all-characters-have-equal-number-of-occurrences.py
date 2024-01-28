class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:        
        c = Counter(s)
        for i in c.values():
            if(i != max(c.values())):
                return False
        return True
            