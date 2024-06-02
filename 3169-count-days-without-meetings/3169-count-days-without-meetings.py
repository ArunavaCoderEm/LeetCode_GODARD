class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if(len(meetings) == 1 and meetings[0][1] == days and meetings[0][0] == 1):
            return 0 
        if len(meetings) == 1 and meetings[0][0] == 1 and meetings[0][1] == 1:
            return days - 1
        meetings.sort()
        free, meet = 0,0
        for i in meetings:
            if(i[0] > meet + 1): free += (i[0] - meet - 1)
            meet = max(meet,i[1])
        if(i[1] < days): free += days-meet
        return free