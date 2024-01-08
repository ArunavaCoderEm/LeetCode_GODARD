class Solution(object):
    def isPalindrome(self, s):
        if (bool(s and not s.isspace()) == False):
            return True
        else :
            test_str = ''.join(letter for letter in s if letter.isalnum()).lower()
        if (test_str == test_str[::-1]):
            return True
        else :
            return False