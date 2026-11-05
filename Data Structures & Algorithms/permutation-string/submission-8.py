class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)): return False

        count = [0] * 26
        count2 = [0] * 26
        for c in s1:
            count[ord(c) - ord('a')] += 1
        
        l, r = 0, len(s1) - 1
        for c in s2[l:r+1]:
            count2[ord(c) - ord('a')] += 1
        if count == count2: return True

        count2[ord(s2[l]) - ord('a')] -= 1
    
        l += 1
        r += 1
        while(r < len(s2)):

            count2[ord(s2[r]) - ord('a')] += 1

            if count2 == count: return True
            
            count2[ord(s2[l]) - ord('a')] -= 1

            l += 1
            r += 1

        return False


            
