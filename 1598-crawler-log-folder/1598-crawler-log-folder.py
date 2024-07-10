class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if(i != "../" and i != './'): stack.append(i)
            elif(i == './'): continue
            elif(len(stack) and i == '../'):
                stack.pop()
            print(stack)
        return len(stack)