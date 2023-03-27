
class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:
        res = []
        candidates.sort()

        def backtracking(nums, start, target, members, res_):
            # print(nums, target, members, res_, idx)
            if target == 0:
                res_.append(members)

            if target < 0:
                return -1

            if sum(nums) < target:
                return -1

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                else:
                    backtracking(nums, i + 1, target - nums[i], members + [nums[i]], res_)

        backtracking(candidates, 0, target, [], res)

        return res








