# class Solution:
#     def countCompleteDayPairs(self, hours: List[int]) -> int:
#         count = 0
#         for i in range(len(hours) - 1):
#             for j in range(i+1, len(hours)):
#                 if((hours[i] + hours[j]) % 24 == 0): count += 1
#         return count

class Solution:
    # Hint 2 .. has given the answer only LOL
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
        res = [0]*24
        for j in hours:
            count += res[(24-(j%24)) % 24]
            res[j % 24] += 1
        return count