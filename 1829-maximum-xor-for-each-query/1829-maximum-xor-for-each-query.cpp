// easy ... vro i am getting good ! so i'll stop dev for a while
// O(3n) TC and O(1) SC
class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {

        int n = nums.size();

        for (int i = 1; i < n; ++i) {

            nums[i] = nums[i-1] ^ nums[i];

        }

        for (int i = 0; i < n; ++i) {

            int ele = pow(2, maximumBit) - 1;
            nums[i] = nums[i] ^ ele; 

        }

        reverse(nums.begin(), nums.end());

        return nums;

    }
};