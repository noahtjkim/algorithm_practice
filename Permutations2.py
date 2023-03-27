
class Solution:
    def permuteUnique(self, nums: list) -> list:
        res = []

        def backtracking(arr, p):
            if p == len(arr):
                res.append(list(arr))

            for i in range(p, len(arr)):
                # swap the first one and the next one
                if i != p:
                    arr[i], arr[p] = arr[p], arr[i]

                backtracking(arr, p + 1)

                # swap the first one and the next one to the original
                if i != p:
                    arr[i], arr[p] = arr[p], arr[i]

        backtracking(nums, 0)

        ans = []
        for e in res:
            if e not in ans:
                ans.append(e)

        return ans







