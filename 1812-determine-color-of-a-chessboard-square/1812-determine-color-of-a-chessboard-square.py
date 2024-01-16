class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        i = coordinates[0]
        j = int(coordinates[1])
        if (i == 'a' or i == 'c' or i == 'e' or i == 'g'):
            if (j % 2 == 0):
                return True
            else: return False
        else :
            if (j % 2 == 0):
                return False
            else: return True