class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        aList = list(s)
        for i in range (0,len(aList)):
            aList = [aList[-1]] + aList[:-1]
            if("".join(aList) == goal): return True
        return False       