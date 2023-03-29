
from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        cnt_map = Counter(s)
        cnt = 0
        used = set()

        # iterate key, values
        for k, v in cnt_map.items():
            # check if v is greater than 0
            # and the v is in used
            # used for the unique values
            while v > 0 and v in used:
                v -= 1
                cnt += 1
            used.add(v)

        return cnt







