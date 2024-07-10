import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        dist = self.r * math.sqrt(random.uniform(0, 1))
        angle = random.uniform(0, 2 * math.pi)
        x = self.x + dist * math.cos(angle)
        y = self.y + dist * math.sin(angle)
        return [x, y]

# Example usage

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()