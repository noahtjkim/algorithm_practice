
class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            p = len(nums) - 1

            while True:
                if nums[p - 1] >= nums[p]:
                    p -= 1
                else:
                    break

                if p == 0:
                    break

            if p == 0:
                nums[::] = nums[::-1]
            else:
                p2 = len(nums) - 1
                while nums[p2] <= nums[p - 1]:
                    p2 -= 1
                tmp1 = nums[p2]
                tmp2 = nums[p - 1]
                nums[p - 1] = tmp1
                nums[p2] = tmp2

                nums[p:] = sorted(nums[p:])









