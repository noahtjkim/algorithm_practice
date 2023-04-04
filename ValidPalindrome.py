
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ""
        s = s.lower()

        for e in s:
            if e.isalnum():
                pal += e

        if pal == pal[::-1]:
            return True
        else:
            return False
