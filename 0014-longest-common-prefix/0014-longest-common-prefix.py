class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        t = strs[0]
        i = 0
        
        while i < len(t):
            j = 1
            while j < len(strs):
                if i >= len(strs[j]) or t[i] != strs[j][i]:
                    return t[0:i]
                j += 1
            i += 1
        
        return t
