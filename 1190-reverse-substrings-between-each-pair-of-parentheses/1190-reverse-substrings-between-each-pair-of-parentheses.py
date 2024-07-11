## simple concept of stack and queue

class Solution:
    def reverseParentheses(self, s: str) -> str:

        stk = [] 
        
        que = []
        
        for i in s:
            if (i != ")"):
                stk.append(i)
            if (i == ")"):
                popstk = stk.pop()
                while (popstk != "("):
                    que.append(popstk)
                    popstk = stk.pop()
                    
            while(len(que)):
                popque = que.pop(0)
                stk.append(popque)
        
        retstr = "".join(stk)
        
        return retstr