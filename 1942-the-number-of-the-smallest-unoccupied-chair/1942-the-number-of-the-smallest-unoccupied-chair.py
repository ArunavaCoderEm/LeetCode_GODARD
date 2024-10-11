# Good problem after a long time
# Two approaches of code 

# With Hint

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        n = len(times)
        events = []

        for i, (arrv, dep) in enumerate(times):
            events.append((arrv, 'arrive', i))
            events.append((dep, 'depart', i))

        events.sort(key=lambda x: (x[0], x[1] == 'arrive'))
        
        available_chairs = list(range(n))
        heapq.heapify(available_chairs)

        occupied_chairs = []
        
        for time, event_type, friend_index in events:
            if (event_type == 'depart'):
            
                for j in range(len(occupied_chairs)):
                    if occupied_chairs[j][1] == friend_index:
                        heapq.heappush(available_chairs, occupied_chairs[j][0])
                        occupied_chairs.pop(j)
                        heapq.heapify(occupied_chairs)
                        break
            else:
                chair = heapq.heappop(available_chairs)
                heapq.heappush(occupied_chairs, (chair, friend_index))
                
                if (friend_index == targetFriend):
                    return chair


# Without Hint

''' better understandable approach

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        chairs = [False] * n
        totalSortedTimes = [(times[i][0], times[i][1], i) for i in range(n)]
        totalSortedTimes.sort(key=lambda x: x[0])
        chairOccupants = [-1] * n
        
        for arrv, dep, i in totalSortedTimes:
            for k in range(n):
                if chairOccupants[k] != -1 and dep > arrv and times[chairOccupants[k]][1] <= arrv:
                    chairOccupants[k] = -1
            
            for j in range(n):
                if chairOccupants[j] == -1:
                    chairOccupants[j] = i
                    break
            
            if i == targetFriend:
                return j

'''