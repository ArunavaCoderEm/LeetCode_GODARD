class Solution {
public:
    bool iseven(int n){
        return n % 2 == 0;
    }
    bool isArraySpecial(vector<int>&nums) {
       for(int i = 1; i < nums.size(); ++i){
            if(iseven(nums[i]) && iseven(nums[i - 1])){
                return false;
            }
            if(!iseven(nums[i]) && !iseven(nums[i - 1])){
                return false;
            }
       } 
       return true;
    }
};