
class Solution:
    def combine(self, n: int, k: int) -> list:
        nums = [x for x in range(1, n + 1)]
        res = []

        def backtracking(nums, start, combs):
            combs.append(nums[start])

            if len(combs) == k:
                if combs not in res:
                    # list(combs) is meaning that a new object is created in the memory
                    # therefore an independent new object is added to the res
                    # if res.append(combs), then the appended list
                    # is pointing the combs address
                    # then del combs[-1] occurs then res also will delete the last element
                    res.append(list(combs))

                return res

            for i in range(start + 1, len(nums)):
                backtracking(nums, i, combs)
                # remove the last element of combs
                del combs[-1]

        for i in range(len(nums)):
            backtracking(nums, i, [])

        return res