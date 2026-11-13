class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
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
                stack.append(int(t2/t1))
            else:
                stack.append(int(t))
            
            # print(f"after: {stack}")
            

        #print(stack)
        return stack[0]