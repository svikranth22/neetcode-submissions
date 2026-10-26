class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            length = 1
            if num -1 not in nums:
                curr = num + length
                while(curr in nums):
                    length += 1
                    curr += 1

            longest = max(length, longest)

        return longest

        