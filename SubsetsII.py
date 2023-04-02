
class Solution:
    def subsetsWithDup(self, nums: list) -> list:
        res = []
        nums = sorted(nums)

        def backtracking(n, subs, depth):
            if len(subs) == len(nums):
                if subs not in res:
                    res.append(list(subs))
                return

            if len(subs) == depth:
                if subs not in res:
                    res.append(list(subs))

            for i in range(len(n)):
                subs.append(n[i])
                backtracking(n[i + 1:], subs, depth + 1)
                del subs[-1]


        res.append([])
        backtracking(nums, [], 0)

        return res