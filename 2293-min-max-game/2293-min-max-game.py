class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        temp = nums

        while (len(temp) > 1):

            turn = True
            chklist = []
            for i in range(0, len(temp) - 1, 2):
                if (turn):
                    chklist.append(min(temp[i], temp[i+1]))
                else:
                    chklist.append(max(temp[i], temp[i+1]))
                
                turn = not turn
    
            temp = chklist

        return temp[0]