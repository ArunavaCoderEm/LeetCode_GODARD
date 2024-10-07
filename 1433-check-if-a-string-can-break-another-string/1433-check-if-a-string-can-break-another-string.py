# this was a easy tier thnx to py for letting me sort the strs

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:

        ress1 = ''.join(sorted(s1))
        ress2 = ''.join(sorted(s2))
        
        can_s1 = True
        can_s2 = True
        
        for i in range(len(ress1)):
            if (ress1[i] < ress2[i]):
                can_s1 = False
            if (ress2[i] < ress1[i]):
                can_s2 = False
        
        return can_s1 or can_s2