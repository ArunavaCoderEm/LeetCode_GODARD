class Solution {
public:
// Pretty easy sliding window
    int minSubArrayLen(int target, vector<int>& nums) {
        int i = 0, j = 0;
        int minn = INT_MAX;
        int res = 0;
        while(i <= j && j < nums.size() && res < target){
            res += nums[j];
            if(res >= target){
                while(res >= target){
                    res -= nums[i];
                    minn = min(minn,j-i+1);
                    i++;
                }
            }
            j++;
        }
        if(minn == INT_MAX){
            return 0;
        }
        return minn;
    }
};