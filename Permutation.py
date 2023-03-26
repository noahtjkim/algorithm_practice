
class Solution:
    def permute(self, nums: list) -> list:
        """
        each number can be the first element of permutation
        e.g. 123 132, 213 231, ...
        iterate nums and combine all the other members
        each combination will be put into res
                        1
                2       3       4
             3   4    2   4   2   3
             4   3    4   2   3   2
        """
        res = []

        def backtracking(arr, p):
            if p == len(arr):
                res.append(list(arr))

            for i in range(p, len(arr)):
                if i != p:
                    arr[i], arr[p] = arr[p], arr[i]

                backtracking(arr, p + 1)

                if i != p:
                    arr[i], arr[p] = arr[p], arr[i]

        backtracking(nums, 0)
        return res


sol = Solution()
res = sol.permute([1, 2, 3, 4])
print(res)






