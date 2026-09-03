class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = {}
        l, r = 0, 0
        res = k
        currChar = ''
        currLen = 0
        replacements = 0
        while r < len(s):
            charSet[s[r]] =  charSet.get(s[r], 0) + 1
            if (r - l) + 1 >= k:
                while ((r - l) + 1) - max(charSet.values()) > k:
                    charSet[s[l]] -= 1
                    l += 1
            
            res = max(res, (r - l) + 1)
            r += 1
        
        return res