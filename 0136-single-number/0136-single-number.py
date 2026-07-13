class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k={}
        for i in nums:
            if i not in k:
                k[i]=1
            else:
                k[i]=k[i]+1

        for i in k:
            if k[i]==1:
                return i
