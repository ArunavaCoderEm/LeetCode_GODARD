import numpy as np
class Solution:
    # ez two pointer
    # just do what the question says
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        med = arr[(len(arr) - 1) // 2]
        print(med)
        res = []
        i, j, m = 0, len(arr) - 1, 0
        while(k > m):
            if((abs(arr[i] - med) > abs(arr[j] - med)) or ((abs(arr[i] - med) == abs(arr[j] - med)) and (arr[i] > arr[j]))):
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j -= 1
            m += 1
        return res
            