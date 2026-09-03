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
                    if temp.isdigit():
                        num = int(temp)
                    else:
                        num = 0
                    
                    if num == 0:
                        res.append("")
                    
                    temp = ""
                    reading = not reading
                    continue
                else:
                    if len(temp) == num:
                        temp = ""
                        reading = not reading
                        continue

        
            temp += c
            print(temp)
            if not reading and len(temp) == num:
                res.append(temp)
                num = 0
                temp = ""

        return res