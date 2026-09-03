class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while (r < len(prices)):
            currProfit = prices[r] - prices[l]
            if currProfit < 0:
                l = r
            else:
                maxProfit = max(maxProfit, currProfit)
            r += 1
        return maxProfit