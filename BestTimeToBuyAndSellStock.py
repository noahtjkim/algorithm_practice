
class Solution:
    def maxProfit(self, prices: list) -> int:
        if len(prices) == 1:
            return 0

        l, r = 0, 1
        res = 0

        while r < len(prices):
            open_pl = prices[r] - prices[l]
            if prices[l] < prices[r]:
                res = max(open_pl, res)
            else:
                l = r

            r += 1

        return res
