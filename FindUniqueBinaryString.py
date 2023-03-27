
class Solution:
    def findDifferentBinaryString(self, nums: list) -> str:
        res = ""

        for i, num in enumerate(nums):
            if num[i] == "0":
                res += "1"
            else:
                res += "0"

        return res








