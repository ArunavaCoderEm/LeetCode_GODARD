class Solution:
    def simplifyPath(self, path: str) -> str:
        array = path.split("/")
        
        stack = []
        
        for i in array:
            if(i =="" or i=="."):
                continue
            if(i==".."and stack):
                stack.pop()
            elif (i != ".."):
                stack.append(i)
        
        res = "/".join(stack)
        retres = "/" + res
        return retres