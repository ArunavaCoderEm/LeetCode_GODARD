class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if (0 in arr and arr.count(0) > 1):
            return True
        for i in arr:
            if(2*i in arr and arr.index(i) != arr.index(i*2)):
                return True
        return False
