class Solution:

    def __getCharIndex(self, char):
        return ord(char) - ord('a')

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1CharCount = [0] * 26
        s2CharCount = [0] * 26
        matches = 0
        
        if len(s2) < len(s1):
            return False

        for i in range(len(s1)):
            s1CharCount[self.__getCharIndex(s1[i])] += 1
            s2CharCount[self.__getCharIndex(s2[i])] += 1
        
        for i in range(26):
            if s1CharCount[i] == s2CharCount[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = self.__getCharIndex(s2[r])
            s2CharCount[index] += 1
            if (s2CharCount[index] == s1CharCount[index]):
                matches += 1
            elif s2CharCount[index] == s1CharCount[index]+1:
                matches -= 1
            
            index = self.__getCharIndex(s2[l])
            s2CharCount[index] -= 1
            if (s2CharCount[index] == s1CharCount[index]):
                matches += 1
            elif s2CharCount[index] == s1CharCount[index]-1:
                matches -= 1
            
            l += 1

        return matches == 26



