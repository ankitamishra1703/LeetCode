class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        s=str(x)
        for i in range(len(s)):
            if s[i]!=s[len(s)-i-1]:
                return False
        return True