class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=len(nums)
        for i in range(l):
            if val in nums:
                nums.remove(val)
        print(nums)
        k=len(nums)
        return k