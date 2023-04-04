
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: list) -> bool:

        n_cnt = Counter(nums)

        for key in n_cnt.keys():
            if n_cnt[key] > 1:
                return True

        return False

