class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for c, i in count.items():
            freq[i].append(c)
        
        for i in range(len(freq) - 1, 0, - 1):
            for j in freq[i]:
                if len(res) == k:
                    return res
                
                res.append(j)
        
        return res