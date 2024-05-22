class Solution {
public:
// with cpp it gave me 80% ... is this any kind of joke ??
    int maxArea(vector<int>& height) {
        int newa, area = INT_MIN, i = 0, j = height.size() - 1;
        while(i < j){
            newa = (j - i) * min(height[i], height[j]);
            area = max(area, newa);
            if(height[i] < height[j]) i++;
            else j--;
        }
        return area;
    }
};

/*
gave me 17% with python let's see same with C++
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        area = -99
        while(i < j):
            newa = (j - i) * min(height[i], height[j])
            area = max(area, newa)
            # thanks hint 2
            if(height[i] < height[j]): i += 1
            else: j -= 1
        return (area)

*/