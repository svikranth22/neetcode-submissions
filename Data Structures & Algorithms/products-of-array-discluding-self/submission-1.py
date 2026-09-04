class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [0] * len(nums), [0] * len(nums)

        for i in range(len(nums)):
            if i != 0 :
                prefix[i] = prefix[i - 1] * nums[i]
            else:
                prefix[i] = nums[i]

            j = len(nums) - 1 - i
            if j != len(nums) - 1 :
                postfix[j] = postfix[j + 1] * nums[j]
            else:
                postfix[j] = nums[j]
            
        res = [0] * len(nums)
        for i in range(len(nums)):
            if i - 1 < 0:
                pre = 1
            else:
                pre = prefix[i - 1]
            
            if i + 1 >= len(nums):
                post = 1
            else:
                post = postfix[i + 1]
            
            res[i] = pre * post
        
        return res

        