class Solution:
    def isValid(self, s: str) -> bool:
        o = {')' : '(',
            '}' : '{',
            ']' : '['
            }
        stack = []
        for c in s:
            if c not in o:
                stack.append(c)
            else:
                if not stack or o[c] != stack[-1]:
                    return False
                stack.pop()
        return not stack
