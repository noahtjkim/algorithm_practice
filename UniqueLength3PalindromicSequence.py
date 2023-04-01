
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        seen = set()

        # iterate the string from the left
        for i in range(len(s)):
            # put the right point at the most right side
            r = len(s) - 1

            # if a char is already in seen then continue
            if s[i] in seen:
                continue

            # find a char that makes it palindrome
            while i < r:
                # if there is a char which is the same as the beginning one of palindrome
                if s[i] == s[r]:
                    # add it to the seen
                    seen.add(s[i])

                    # count all possible palidrome cases
                    # e.g.
                    # a   abc    a
                    # aaa, aba, aca
                    res += len(set(s[i + 1:r]))
                    break

                r -= 1

        return res