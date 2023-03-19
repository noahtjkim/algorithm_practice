
class Solution:
    def sortByBits(self, arr: list) -> list:

        res = sorted(arr, key=lambda x: (str(bin(x)).count("1"), x))

        return res

sol = Solution()
res = sol.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])
print(res)







