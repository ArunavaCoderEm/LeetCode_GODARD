# use double ended queue for better results ! but who cares ... logic is the same
# DQ just does it in constant time else loop and all will be the same

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        left = []
        right = []

        for i in nums:
            if(i >= pivot):
                if (i == pivot):
                    right.insert(0, i)
                else:
                    right.append(i)
            else:
                left.append(i)

        nums = left + right

        return nums