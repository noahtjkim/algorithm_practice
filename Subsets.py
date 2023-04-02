
class Solution:
    def subsets(self, nums: list) -> list:
        res = []

        def backtracking(n, subset, level):
            if len(subset) == level:
                if subset not in res:
                    res.append(list(subset))

            if len(subset) == len(nums):
                return

            if not n:
                if subset not in res:
                    res.append(list(subset))
                return

            for i in range(len(n)):
                subset.append(n[i])
                backtracking(n[i + 1:], subset, level + 1)
                del subset[-1]

        backtracking(nums, [], 0)

        return res