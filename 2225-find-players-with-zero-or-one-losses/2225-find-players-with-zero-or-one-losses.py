class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        key = []
        val = []
        ansz = []
        anso = []
        for i in range(len(matches)):
            key.append(matches[i][0])
        for j in range(len(matches)):
            val.append(matches[j][1])
        count = Counter(val)
        for k in range(len(key)):
            if(count[key[k]] == 0):
                ansz.append(key[k])
            if(count[key[k]] == 1):
                anso.append(key[k])
            if(count[val[k]] == 1):
                anso.append(val[k])
        ansz =list(set(ansz))
        anso =list(set(anso))
        ansz.sort()
        anso.sort()
        return([ansz,anso])