class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w_s = sum(nums[:k])
        m_s = w_s
        for i in range(k, len(nums)):
            w_s += nums[i]
            w_s -= nums[i - k]
            m_s = max(m_s, w_s)

        return (max(m_s, w_s)) / k
