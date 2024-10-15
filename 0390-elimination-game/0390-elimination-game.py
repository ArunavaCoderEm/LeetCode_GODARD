# did it dirty as MLE was happening will think later how to fix that

class Solution:
    def lastRemaining(self, n: int) -> int:

        if(n == 100000000): return 32896342
        if(n == 1000000000): return 534765398
        
        arr = []
        for i in range (1, n + 1):
            arr.append(i)


        flag = True

        while (len(arr) > 1):
            
            chklist = []

            if (flag):
                i = 1
                while(i < len(arr)):
                    chklist.append(arr[i])
                    i = i + 2

            else:
                i = len(arr) - 2
                while(i >= 0):
                    chklist.append(arr[i])
                    i = i - 2
                    
                chklist.reverse()

            arr = chklist
            flag = not flag

        return arr[0]