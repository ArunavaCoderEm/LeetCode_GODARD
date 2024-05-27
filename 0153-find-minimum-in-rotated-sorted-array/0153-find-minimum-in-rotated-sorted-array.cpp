class Solution {
public:
    int findMin(vector<int>& nums) {
        int minn = nums[0];
        int s = 0, e = nums.size() - 1;
        int mid = (s + (e-s)/2);
        while(s < e){
            if(nums[0] <= nums[mid]){
                s = mid + 1;
            }
            else {
                e = mid;
            }
            mid = (s + (e-s)/2);
        }
        int res = min(nums[s],nums[0]);
        return res;
    }
};

// class Solution: could have solved ths way but let's not
//     def findMin(self, nums: List[int]) -> int:
//         return min(nums)