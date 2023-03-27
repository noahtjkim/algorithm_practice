
class Solution:
    def firstUniqChar(self, s: str) -> int:
        idx = -1

        for i in range(len(s)):
            if s[i] not in s[i + 1:] + s[:i]:
                idx = i
                break

        return idx








