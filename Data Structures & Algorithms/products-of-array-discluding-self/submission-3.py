class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

            j = len(nums) - 1 - i
            res[j] *= postfix
            postfix *= nums[j]
        
        return res