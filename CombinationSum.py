
class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        res = []

        def backtracking(nums, target, members, res_):
            if target < 0:
                return -1

            if target == 0:
                res_.append(members)
                return res_

            for i in range(len(nums)):
                backtracking(nums[i:], target - nums[i], members + [nums[i]], res_)

        backtracking(candidates, target, [], res)

        return res


sol = Solution()
res = sol.combinationSum([2, 3, 6, 7], target=7)
print(res)







