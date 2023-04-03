
class Solution:
    def combinationSum3(self, k: int, n: int) -> list:
        res = []
        nums = [x for x in range(1, 10)]

        def backtracking(sub_nums, combs):
            if sum(combs) == n and len(combs) == k:
                if combs not in res:
                    res.append(list(combs))
                return

            if len(combs) > len(nums):
                return

            if not sub_nums:
                return

            for i in range(len(sub_nums)):
                combs.append(sub_nums[i])
                backtracking(sub_nums[i + 1:], combs)
                combs.pop()

        backtracking(nums, [])

        return res