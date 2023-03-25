
class Solution:
    def generateParenthesis(self, n: int) -> list:
        """
        recursive call
        e.g. n = 2 -> (()), ()()
        dfs(2, 2) ()() <- return
        dfs(2, 2) (()) <- return
        dfs(2, 1) ()(
        dfs(2, 1) (()
        dfs(1, 1) ()
        dfs(2, 0) ((
        dfs(1, 0) (
        dfs(0, 0) "" <- start
        """

        def dfs(l: int, r: int, p: str):
            if len(p) == n * 2:
                res.append(p)
                return res

            if l < n:
                dfs(l + 1, r, p + "(")

            if r < l:
                dfs(l, r + 1, p + ")")

        res = []
        dfs(0, 0, "")

        return res








