
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(str(n))
        product = 1
        sum_ = 0

        for num in n:
            product *= int(num)
            sum_ += int(num)

        res = product - sum_
        return res








