
class Solution:
    def isSubsequence(self, s: list, t: list) -> bool:
        s = list(s)
        t = list(t)
        res = []
        seq = 0

        if len(s) > 0:
            for i in range(len(t)):
                if t[i] == s[seq]:
                    res.append(t[i])
                    seq += 1
                    if seq >= len(s):
                        break

        if res == s:
            return True
        else:
            return False







