class Solution:
    ## easiest solution I guess
    def compareVersion(self, version1: str, version2: str) -> int:
        res = version1.split(".")
        ress = version2.split(".")
        rest = 0
        if (len(res) < len(ress)):
            for i in range(len(ress) - len(res)):
                res.append('0')
        elif(len(ress) < len(res)):
            for i in range(len(res) - len(ress)):
                ress.append("0")
        for j in range(len(res)):
            if(int(res[j]) < int(ress[j])):
                rest = -1
                break
            elif(int(ress[j]) < int(res[j])):
                rest = 1
                break
        return rest