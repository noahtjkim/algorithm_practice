
class Solution:
    def minStartValue(self, nums: list) -> int:
        """
        the sum of steps should be greater than or equal to 1
        start from the initial positive number
        """

        sum_ = 0
        prev_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            prev_ = min(prev_, sum_)

        start_value = abs(prev_) + 1

        return start_value








