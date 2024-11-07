
// Brute Force
// class Solution {
// public:
//     int maxRotateFunction(vector<int> &nums) {
            
//         int n = nums.size();
//         int maxResult = INT_MIN;
        
//         for (int i = 0; i < n; ++i) {
            
//             int j = i, summ = 0;
//             int counter = 0;
            
//             do {
                
//                 summ += (counter * nums[j]);
                
//                 counter++;
//                 j = (j + 1) % n; 
                
//             } while (j != i);
            
//             maxResult = max(maxResult, summ);
            
//         }
        
//         return maxResult;
        
//     }
// };

// Better
class Solution {
public:
    int maxRotateFunction(vector<int> &nums) {
        int n = nums.size();
        int sum = 0;
        int Func = 0;
        
        for (int i = 0; i < n; ++i) {
            sum += nums[i];
            Func += i * nums[i];
        }
        
        int maxResult = Func;

        for (int k = 1; k < n; ++k) {
            Func = Func + sum - (n * nums[n - k]);
            maxResult = max(maxResult, Func);
        }
        
        return maxResult;
    }
};

// Now I am able to think properly and in the correct direction at first try only
// TIP - Always start with brute force ALWAYS dont even consider there is better
// once brute force logic is clear to you then only start for a better one
// It becomes way easier that way