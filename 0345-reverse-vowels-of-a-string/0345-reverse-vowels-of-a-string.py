class Solution:
    def reverseVowels(self, s: str) -> str:
        l=[]
        for i in s:
            if i in 'AEIOUaeiou':
                l.append(i)
        t=l[::-1]
        s1=list(s)
        j=0
        
        for i in range(len(s1)):
            if s1[i] in 'AEIOUaeiou':
                s1[i]=t[j]
                j+=1    
        s2=''.join(s1)
        return s2