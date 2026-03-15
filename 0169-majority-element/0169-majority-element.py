class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k={}
        for i in range(len(nums)):
            if nums[i] in k:
                k[nums[i]]+=1
            else:
                k[nums[i]]=1
        for i in k:
            if k[i]>len(nums)//2:
                return i
