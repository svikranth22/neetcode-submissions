class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            if n-1 not in nums:
                i = 1
                while (n + i) in nums:
                    i += 1
                res = max(i , res)
        return res