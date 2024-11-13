// Brute force O(n^2)

// class Solution {
// public:
//     long long countFairPairs(vector<int>& nums, int lower, int upper) {
        
//         int count = 0;

//         int n = nums.size();

//         for (int i = 0; i < n; ++i) {
//             for (int j = i + 1; j < n; ++j) {
//                 if (nums[i] + nums[j] <= upper && nums[i] + nums[j] >= lower) {
//                     count++;
//                 }
//             }
//         }

//         return count;

//     }
// };

// Optimal with help of STL Binary Search O(nlogn)

class Solution {
public:
    long long countFairPairs(vector<int> &nums, int lower, int upper) {
        
        sort(nums.begin(), nums.end());
        long long n = nums.size();
        long long count = 0;

        for (int start = 0; start < n; ++start) {

            long low = lower - nums[start];  
            long high = upper - nums[start]; 
            
            long left = lower_bound(nums.begin() + start + 1, nums.end(), low) - nums.begin();
            long right = upper_bound(nums.begin() + start + 1, nums.end(), high) - nums.begin();

            count += (right - left);
        }

        return count;
    }
};