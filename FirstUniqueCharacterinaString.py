
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Faster code
        cnt_dict = Counter(s)
        idx = -1

        for i in range(len(s)):
            if cnt_dict[s[i]] == 1:
                idx = i
                break

        return idx

        # Slower code
        # idx = -1
        #
        # for i in range(len(s)):
        #     if s[i] not in s[i + 1:] + s[:i]:
        #         idx = i
        #         break
        #
        # return idx








