class Solution(object):
    def lengthOfLastWord(self, s):
        return int(len(s.split()[len(s.split())-1]))
        