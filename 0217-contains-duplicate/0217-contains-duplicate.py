class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        k={}
        for i in nums:
            if i not in k:
                k[i]=1
            else:
                k[i]=k[i]+1

        for i in k:
            if k[i]>=2:
                return True
        return False
