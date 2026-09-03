class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Make a Hash Map to count num of occurences for each letter
        count = {}

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
        
        for _, value in count.items():
            if value != 0:
                return False
        
        return True