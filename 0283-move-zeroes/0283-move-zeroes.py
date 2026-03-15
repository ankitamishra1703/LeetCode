class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        wr=0
        for r in range(len(nums)):
            if nums[r]!=0:
                nums[wr],nums[r]=nums[r],nums[wr]
                wr+=1


            