
class Solution:
    res = []
    nums = [[], [], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"],
            ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"],
            ["t", "u", "v"], ["w", "x", "y", "z"]]

    def backtracking(self, combination, next_d):
        if not next_d:
            self.res.append(combination)
            return self.res

        for c in self.nums[int(next_d[0])]:
            self.backtracking(combination + c, next_d[1:])

    def letterCombinations(self, digits: str) -> list:
        """
        Backtracking: to find all solutions using brute force approach
        """
        if not digits:
            return []

        self.res = []
        self.backtracking("", digits)
        return self.res








