class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vow = ['a','A','e',"E",'i','I','o',"O",'u',"U"]
        count = 0
        for i in range (left,right+1):
            if(words[i][0] in vow and words[i][len(words[i])-1] in vow):
                count += 1
        return count