// using bubble sort concept now can it be further optimized 
// I'll think first lemme submit

class Solution {
    private:
        bool hasSameSetBits(int x, int y) {
            return __builtin_popcount(x) == __builtin_popcount(y);
        }
    public:
        bool canSortArray(vector<int>& nums) {
            
            int n = nums.size();

            for (int i = 0; i < n - 1; i++) {
                bool flag = false;
                for (int j = 0; j < n - 1; ++j) {
                     if (nums[j] > nums[j + 1]) {
                        flag = true;
                        if (hasSameSetBits(nums[j], nums[j + 1])) {
                            swap(nums[j], nums[j + 1]);
                        } else {
                            return false;
                        }
                    }
                }
                if (! flag) return true;
            }

            return true;

        }
};