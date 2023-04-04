
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        res = []
        l, r = 0, len(nums) - 1

        while l < r:
            sum_ = nums[l] + nums[r]
            if sum_ == target:
                res.append(l)
                res.append(r)
                break

            r -= 1

            if r <= l:
                l += 1
                r = len(nums) - 1

        return res

