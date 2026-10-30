class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        result = 0
        while(l < r):
            h1, h2 = heights[l], heights[r]
            height = min(h1, h2)
            length = r - l
            volume = height * length

            result = max(result, volume)

            if (h1 < h2):
                l += 1
            else:
                r -= 1
        return result
            
