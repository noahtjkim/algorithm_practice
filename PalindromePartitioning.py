
class Solution:
    def partition(self, s: str) -> list:
        res = []

        def backtracking(start, s, pals):
            if start >= len(s):
                res.append(list(pals))
                return

            for i in range(start, len(s)):
                pal = s[start:i + 1]
                if pal == pal[::-1]:
                    pals.append(pal)
                    backtracking(i + 1, s, pals)
                    pals.pop()

        backtracking(0, s, [])

        return res