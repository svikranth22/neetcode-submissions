class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)] 
        for key, value in count_map.items():
            buckets[value].append(key)
    
        res = []
        for b in buckets[::-1]:
            for n in b:
                res.append(n)
                if len(res) == k:
                    return res