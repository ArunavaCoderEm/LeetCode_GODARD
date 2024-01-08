class Solution(object):
    def checkIfPangram(self, sentence):
        op = []
        for char in sentence:
            op.append(char)
        opp = list(set(op))
        opp.sort()
        return "abcdefghijklmnopqrstuvwxyz" == "".join(opp)
        