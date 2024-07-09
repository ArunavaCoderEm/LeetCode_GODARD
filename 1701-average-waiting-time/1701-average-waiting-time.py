class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        end = customers[0][1]
        customers[0][1] += customers[0][0]
        for i in range(1,len(customers)):
            if(customers[i-1][1] - customers[i][0] > 0):
                end += (customers[i-1][1] - customers[i][0])
                customers[i][0] += (customers[i-1][1] - customers[i][0])
            end += customers[i][1]
            customers[i][1] += customers[i][0]
        return end/len(customers)    