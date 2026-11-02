class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        result = 0
        low = sys.maxsize
        for num in prices:
            curr_profit = num - low
            if curr_profit < 0:
                low = num
            else:
                result = max(curr_profit, result)
        return result