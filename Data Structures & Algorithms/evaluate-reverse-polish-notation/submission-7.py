class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            if tokens[0] not in '*+/-':
                return int(tokens[0])
            else: return 0
        
        result = int(tokens[0])
        stack = []
        tmp = 0
        for i in range(0, len(tokens)):
            t = tokens[i]
            # print(f"--iteration: {i} --")
            # print(f"Before: {stack}")
            # print(f"token: {t}")
            if t == '*':
                t1 = stack.pop()
                t2 = stack.pop()

                stack.append(t2 * t1)
            elif t =='+':
                t1 = stack.pop()
                t2 = stack.pop()

                stack.append(t2 + t1)
            elif t =='-':
                t1 = stack.pop()
                t2 = stack.pop()

                stack.append(t2 - t1)
            elif t =='/':
                t1 = stack.pop()
                t2 = stack.pop()

                isNeg = False

                if t1 < 0:
                    t1 *= -1
                    isNeg = not isNeg
                if t2 < 0:
                    t2 *= -1
                    isNeg = not isNeg

                r = t2 // t1
                if isNeg:
                    r *= -1
                stack.append(r)
            else:
                stack.append(int(t))
            
            # print(f"after: {stack}")
            

        #print(stack)
        return stack[0]