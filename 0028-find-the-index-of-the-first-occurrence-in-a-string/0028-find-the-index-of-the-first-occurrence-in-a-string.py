class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s1=len(haystack)
        s2=len(needle)
        
        for i in range(s1-s2+1):
            if haystack[i:i+len(needle)]==needle:
                    return i
        return -1