def is_valid_triangle(side1, side2, side3):
    if (side1 + side2 > side3):
        return True
    else:
        return False

# 11 from pending I guess !! today's great
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        c = 0
        for k in range(2, len(nums)):
            i, j = 0, k - 1
            while i < j:
                if (is_valid_triangle(nums[i], nums[j], nums[k])):
                    c += (j - i)
                    j -= 1
                else:
                    i += 1
        return c