class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            result = m.get(diff, 0)

            if result != 0:
                return [result[0], i]
            
            m[nums[i]] = (i, diff)