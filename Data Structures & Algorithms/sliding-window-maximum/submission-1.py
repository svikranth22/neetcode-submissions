class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q  = collections.deque()
        l = 0
        for r in range(len(nums)):
            if q and q[0] <= r - k:
                q.popleft()
            while (q and nums[r] > nums[q[-1]]):
                p = q.pop()
            q.append(r)

            if r >= k - 1:
                result.append(nums[q[0]])
                l += 1
        return result