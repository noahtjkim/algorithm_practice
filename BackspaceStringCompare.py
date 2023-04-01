
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for e in s:
            if e == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(e)

        for e in t:
            if e == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(e)

        if stack_s == stack_t:
            return True
        else:
            return False
