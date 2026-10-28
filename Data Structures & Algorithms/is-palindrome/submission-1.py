class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) -1

        while(i < j):
            s1 = s[i]
            s2 = s[j]
            if not s1.isalnum():
                i += 1
                continue
            if not s2.isalnum():
                j -= 1
                continue
            if s1.lower() != s2.lower():
                return False
            
            i += 1
            j -= 1
        return True