
class Solution:
    def firstPalindrome(self, words: list) -> str:
        res = ""

        for i in range(len(words)):
            pal = []

            if words[i] == words[i][::-1]:
                res = words[i]
                break

        return res