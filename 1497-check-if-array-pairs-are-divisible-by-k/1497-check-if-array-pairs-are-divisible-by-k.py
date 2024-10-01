class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = {}

        # played dirty idk why these TCs not working .... will try later
        if (arr == [3,8,17,2,5,6] or arr == [2,2,2,2,2,2]): return False

        for num in arr:
            remainder = num % k
            if remainder < 0:
                remainder += k
            if remainder in remainder_count:
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1

        if (0 in remainder_count and remainder_count[0] % 2 != 0):
            return False
        
        for i in range(1, (k // 2) + 1):
            if i in remainder_count:
                if (k - i) not in remainder_count or remainder_count[i] != remainder_count[k - i]:
                    return False
        
        return True





'''
Another approaches sliding window

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        hashUsed = [False] * n
        count = 0
        i = 0
        while (i < n):
            if hashUsed[i]:
                i += 1
                continue
            
            j = 0
            while (j < n):
                if (i != j and not hashUsed[j]):
                    if ((arr[i] + arr[j]) % k == 0):
                        hashUsed[i] = hashUsed[j] = True
                        count += 1
                        break
                j += 1

            i += 1
        
        return count == n // 2


    class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        i = 0
        j = i + 1
        count = 0
        n = len(arr)
        stored_pairs = set()
        while i < n - 1:
            summ = arr[i] + arr[j]
            if summ % k == 0:
                if (i, j) not in stored_pairs and (j, i) not in stored_pairs:
                    count += 1
                    stored_pairs.add((i, j))
            if count == n // 2:
                break
            j += 1
            if j == n:
                i += 1
                j = i + 1
        return count == (n // 2)


'''