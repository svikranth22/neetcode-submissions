class Solution:

    def encode(self, strs: List[str]) -> str:
        es = ""
        for s in strs:
            es += f"#{len(s)}#{s}"
        return es

    def decode(self, s: str) -> List[str]:
        reading = False
        res = []
        temp = ""
        num = 0
        for c in s:
            if c == '#':
                if reading:
                    num = int(temp)
                    
                    if num == 0:
                        res.append("")

                if reading or len(temp) == num:
                    temp = ""
                    reading = not reading
                    continue

            temp += c
            if not reading and len(temp) == num:
                res.append(temp)
                num = 0
                temp = ""

        return res