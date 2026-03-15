class Solution:
    def reverseWords(self, s: str) -> str:
        s1=s.split()
        l=s1[::-1]
        r=''
        for i in l:
            r+=' '+i
        return r.strip()

