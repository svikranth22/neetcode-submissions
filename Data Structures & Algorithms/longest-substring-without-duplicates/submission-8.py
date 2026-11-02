class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) <= 1): return len(s)
        t = set()
        result = 0
        l,r = 0, 1
        for i, c in enumerate(s):
            if c in t:
                result = max(result, len(t))
                while s[l] != c:
                    t.remove(s[l])
                    l += 1
                t.remove(s[l])
                l += 1
            t.add(c)
        return max(result, len(t))