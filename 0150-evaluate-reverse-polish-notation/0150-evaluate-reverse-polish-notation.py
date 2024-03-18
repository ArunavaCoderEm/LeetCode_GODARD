class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        if(len(tokens) <= 1): return int(tokens[0])
        char = ['+','-','*','/']
        while (i < (len(tokens)) - 1):
            while(tokens[i] in char and i < len(tokens) - 1):
                x = stack.pop()
                y = stack.pop()
                res = eval(f"{y} {tokens[i]} {x}")
                i += 1
                stack.append(int(res))
            if(tokens[i] not in char):
                stack.append(int(tokens[i]))
                i += 1
            if(i > len(tokens) - 1): break
        x = stack.pop()
        y = stack.pop()
        res = eval(f"{y} {tokens[i]} {x}")
        return int(res)