
class Solution:
    def minimumAbsDifference(self, arr: list) -> list[list: int]:
        res = []
        diff = 0
        arr.sort()

        # find the minimum first
        for i in range(len(arr)):
            if i > 0:
                curr = arr[i] - arr[i - 1]
                if diff == 0:
                    diff = curr
                else:
                    diff = min(diff, curr)

        for i in range(len(arr)):
            if i > 0:
                curr = arr[i] - arr[i - 1]
                if curr == diff:
                    res.append([arr[i - 1], arr[i]])

        return res







