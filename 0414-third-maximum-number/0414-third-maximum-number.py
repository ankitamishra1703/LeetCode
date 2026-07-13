class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        k = []

        for _ in range(3):
            if not nums:
                break

            l = nums[0]

            for num in nums:
                if num > l:
                    l = num

            k.append(l)

            while l in nums:
                nums.remove(l)

        if len(k) >= 3:
            return k[2]
        else:
            return k[0]