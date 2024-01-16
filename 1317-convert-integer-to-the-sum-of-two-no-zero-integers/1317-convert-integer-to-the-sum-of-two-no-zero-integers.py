class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        default = 1
        while '0' in (f'{default}{n-default}'):
            default += 1
        return [default, n-default]