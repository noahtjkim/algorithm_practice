
class Solution:
    def maxSubArray(self, nums: list) -> int:
        if len(nums) < 2:
            return nums[-1]

        max_ = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            res = max(nums[i], res + nums[i])
            max_ = max(max_, res)

        return max_








