// after 6 wrong ans and 2 TLE 
// Now this was a good one ... Revise List

const long long MOD = 1e9 + 7;

class Solution {
public:
    int minAbsoluteSumDiff(vector<int>& nums1, vector<int>& nums2) {
        vector<long long int> result;
        long long int reqSum = 0;
        for (int i = 0; i < nums1.size(); ++i){
            long int res = abs(nums1[i] - nums2[i]);
            result.push_back(res);
            reqSum += res;
        }
        sort(nums1.begin(), nums1.end(), [](int a, int b) {
            return (a - b) < 0; 
        });
        long long int totalRem = reqSum;
        for (int j = 0; j < nums1.size(); ++j) {
            int start = 0, end = nums1.size() - 1;
            long int oldDiff = result[j];
            long int newDiff = oldDiff;
            while (start <= end) {
                int mid = (start + (end - start) / 2);
                int diffr = (nums1[mid] - nums2[j]);
                int adiffr = abs(nums1[mid] - nums2[j]);
                if (adiffr < newDiff) {
                    newDiff = adiffr;
                    if (newDiff == 0) {
                        break;
                    }
                }
                if (diffr < 0) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
            totalRem = min(static_cast<long long>(totalRem), ((reqSum - oldDiff) + newDiff));
        }
        return totalRem % MOD;
    }
};