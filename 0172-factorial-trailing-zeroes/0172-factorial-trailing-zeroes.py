# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     return n*factorial(n-1)

# class Solution:
#     def trailingZeroes(self, n: int) -> int:
#         x = (factorial(n))
#         count = len(x) - len(x.rstrip('0'))
#         return int(count)

## cheapest solution
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return (n//5)+(n//25)+(n//125)+(n//625)+(n//3125)