def dist(a,x):
    return abs(a - x)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while (left < right):
            mid = (left + right) // 2
            if (arr[mid] < x):
                left = mid + 1
            else:
                right = mid
        left, right = left - 1, left
        while (right - left - 1 < k):
            if (left == -1):
                right += 1
            elif (right == len(arr) or (dist(arr[left],x) <= dist(arr[right],x))):
                left -= 1
            else:
                right += 1  
        # one manual IDK why
        left = left + 1  
        return arr[left:right]