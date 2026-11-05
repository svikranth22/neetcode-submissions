class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)): return False

        count1 = collections.defaultdict(int)
        count2 = collections.defaultdict(int)
        match = 0
        for i in range(len(s1)):
            count1[s1[i]] += 1
            count2[s2[i]] += 1
        
        for i in range(26):
            c = chr(ord('a') + i)
            if count2[c] == count1[c]:
                match += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if match == 26:
                return True
            
            c = s2[l]
            count2[c] -= 1
            if count1[c] == count2[c]:
                match += 1
            elif count1[c] == count2[c] + 1:
                match -= 1
            
            c = s2[r]
            count2[s2[r]] += 1
            if count1[c] == count2[c]:
                match += 1
            elif count1[c] == count2[c] - 1:
                match -= 1
            
            l += 1

        return match == 26


            
