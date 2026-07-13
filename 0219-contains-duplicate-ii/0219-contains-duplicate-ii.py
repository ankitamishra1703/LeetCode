class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                p = d[nums[i]]
                if i - p <= k:
                    return True

            d[nums[i]] = i

        return False