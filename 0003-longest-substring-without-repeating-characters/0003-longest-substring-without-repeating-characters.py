class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1 = set()
        l = 0
        m = 0

        for i in range(len(s)):
            while s[i] in s1:
                s1.remove(s[l])
                l += 1

            s1.add(s[i])
            m = max(m, i - l + 1)

        return m

            