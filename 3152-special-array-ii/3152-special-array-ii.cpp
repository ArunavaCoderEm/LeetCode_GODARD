class Solution {
public:
    vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {    
        vector<int> ans;
        ans.push_back(0);
        for(int i = 1 ; i < nums.size() ; i++){
            if((nums[i] % 2) == (nums[i-1] % 2)){
                ans.push_back(1);
            }
            else{
                ans.push_back(0);
            }
        }
        vector<int> pair(nums.size());
        pair[0] = 0;
        for(int i = 1 ; i < nums.size() ; i++){
            pair[i] = pair[i-1] + ans[i];
        }
        vector<bool> res;
        for(int i = 0 ; i < queries.size() ; i++){
            int s = queries[i][0];
            int e = queries[i][1];
            if(pair[e] - pair[s] >= 1) res.push_back(false);
            else res.push_back(true);
        }
        return res;
    }
};

// Two lang two approach 

// def iseven(n):
//     return n % 2 == 0
// def sparr(nums, s, e):
//     for i in range(s+1,e+1):
//         if(iseven(nums[i]) and iseven(nums[i - 1])):
//             return False
//         if(not iseven(nums[i]) and not iseven(nums[i - 1])):
//             return False
//     return True
// class Solution:
//     def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
//         res = []
//         for k in queries:
//             ans = sparr(nums, k[0], k[1])
//             res.append(ans)
//         return res