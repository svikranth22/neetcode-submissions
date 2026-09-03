class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for word in strs:
            letter_count_list = [0] * 26
            for c in word:
                letter_count_list[ord(c) - ord('a')] += 1
            
            letter_count = tuple(letter_count_list)
            if letter_count in hmap:
                hmap[letter_count].append(word)
            else:
                hmap[letter_count] = [word]
        
        return [values for key, values in hmap.items()]

