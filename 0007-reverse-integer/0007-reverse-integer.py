class Solution:
    def reverse(self, x: int) -> int:
        
            n=abs(x)
            rev=0
            while n!=0:
                r=n%10
                rev=rev*10+r
                n//=10
            
            if -2**31 <= rev <= (2**31)-1:
                if x<0:
                    return rev*-1
                return rev
                
            return 0