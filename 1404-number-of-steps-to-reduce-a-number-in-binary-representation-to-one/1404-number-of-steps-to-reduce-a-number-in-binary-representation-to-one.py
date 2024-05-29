## Two differennt approaches

def btd(n):
    return int(n,2)

# def checkodd(n):
#     return (n % 2 != 0)

# class Solution:
#     def numSteps(self, s: str) -> int:
#         step = 0
#         num = btd(s)
#         while(num != 1):
#             if(checkodd(num)): num += 1
#             else: num //= 2
#             step += 1
#         return step

class Solution:
    def numSteps(self, s: str) -> int:       
        step = 0
        num = btd(s)
        while(num != 1):
            rem = (num & 1)
            if(rem == 1): num += 1
            else: num = num >> 1
            step += 1; 
        return step


# class Solution {
# public:
#     int numSteps(string s) {
#        long long int num = stoi(s, nullptr, 2);
#        int step = 0;
#         while(num != 1){
#             int rem = (num & 1);
#             if(rem == 1) num++;
#             else num = num >> 1;
#             step++;
#         } 
#         return step;
#     }
# };