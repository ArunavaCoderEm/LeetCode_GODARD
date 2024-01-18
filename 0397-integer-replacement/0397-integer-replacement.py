## MAY BE NOT THE BEST SOLUTION

class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        if (n == 1):
            return 0
        while (n != 1):
            if(n % 2 == 0):
                n = n//2
                count += 1
            else:
                if(((n-1) // 2) % 2 == 0):
                    n = n - 1
                    count += 1
                elif(n == 3):
                    count += 2
                    n = 1
                elif(((n+1) // 2) % 2 == 0):
                    n = n + 1
                    count += 1
        return count