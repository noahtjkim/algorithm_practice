
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        seen = set()

        def dfs(start):
            if start == n:
                return 0

            count = 0
            for i in range(start + 1, n + 1):
                substr = s[start:i]
                if substr not in seen:
                    seen.add(substr)
                    count = max(count, 1 + dfs(i))
                    seen.remove(substr)

            return count

        return dfs(0)


sol = Solution()
res = sol.maxUniqueSplit("ababccc")
print(res)










