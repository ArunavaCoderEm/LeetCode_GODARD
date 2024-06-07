class Solution:
    ## BRUV WTF 36% !! I know in opt soln someone has used
    # some inbuilt lib that I hate !!
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        res = sentence.split()
        res = list(res)
        j = 0
        for i in range(len(res)):
            ans = [p for p in dictionary if res[i].startswith(p)]
            if (ans):
                res[i] = min(ans, key=len)
        return " ".join(res)