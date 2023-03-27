
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = -1

        for i in range(len(haystack)):
            if needle in haystack:
                if needle == haystack[i:i + len(needle)]:
                    idx = i
                    break

        return idx







