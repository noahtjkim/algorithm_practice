
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        res = ""
        l1 = []

        for i in range(len(s)):
            if s[i] not in l1:
                l1.append(s[i])
            else:
                res = s[i]
                break

        return res







