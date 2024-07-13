class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(ast)):
            if not stack or ast[i] > 0 or (stack[-1] < 0 and ast[i] < 0):
                stack.append(ast[i])
            else:
                while stack and stack[-1] > 0 and abs(stack[-1]) < abs(ast[i]):
                    stack.pop()
                
                if not stack or stack[-1] < 0:
                    stack.append(ast[i])
                elif abs(stack[-1]) == abs(ast[i]):
                    stack.pop()
        
        return stack
