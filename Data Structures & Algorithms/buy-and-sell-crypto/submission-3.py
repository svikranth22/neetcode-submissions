class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        result = 0
        low = sys.maxsize
        for num in prices:
            low = min(num, low)
            result = max(num - low, result)
        return result