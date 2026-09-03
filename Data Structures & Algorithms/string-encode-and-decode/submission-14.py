class Solution:

    def encode(self, strs: List[str]) -> str:
        es = ""
        for s in strs:
            es += f"{len(s)}#{s}"
        return es

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            i = j + 1
            j = i + l
            res.append(s[i:j])
            i = j
        
        return res