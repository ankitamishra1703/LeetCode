class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':')','{':'}','[':']'}
        l=[]
       
        for i in s:
            if i in d:
                l.append(d[i])
            else:
                if len(l)==0:
                    return False
                a=l.pop()
                if a!=i:
                    return False      
        return len(l) == 0  