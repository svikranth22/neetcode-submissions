class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        
        result = ""
    
        count_t = collections.Counter(t)
        count_s = collections.defaultdict(int)
        
        l = 0
        min_window_size = float("inf")
        window_size = 0
        matches = 0
        result_found = False
        for r in range(len(s)):
            c = s[r]
            if c in count_t:
                count_s[c] += 1
                if count_s[c] == count_t[c]:
                    matches += 1
            if matches == len(count_t):
                while l < r:
                    if s[l] in count_t:
                        if count_s[s[l]] - 1 < count_t[s[l]]:
                            break;
                        else:
                            count_s[s[l]] -= 1
                    l += 1

                window_size = r - l + 1
                if window_size < min_window_size:
                    result = s[l:r+1]
                    min_window_size = window_size

        return result

        