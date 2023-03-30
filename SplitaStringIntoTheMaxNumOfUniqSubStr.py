
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        max_ = 0
        seen = set()

        def dfs(s, seen):
            ans = 0

            for i in range(1, len(s) + 1):
                candidates = s[:i]

                if candidates not in seen:
                    seen.add(candidates)
                    ans = max(ans, 1 + dfs(s[i:], seen))
                    seen.remove(candidates)
            return ans

        max_ = dfs(s, seen)

        return max_







