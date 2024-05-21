class Solution {
public:
    int findpivot(vector<int>& arr){
        int s = 0, e = arr.size() - 1;
        int mid = (s + (e - s) / 2);
        while(s < e) {
            if(arr[mid] >= arr[0]) s = mid + 1;
            else e = mid;
            mid = (s + (e - s) / 2);
        } 
        return s;
    }
    int bs(vector<int>& mount, int s, int e, int t){
        int st = s, en = e;
        while(st <= en){
            int mid = (st + (en - st) / 2);
            if(mount[mid] == t) return mid;
            if(mount[mid] < t) st = mid + 1;
            else en = mid - 1;
        }
        return -1;
    }
    int search(vector<int>& nums, int target) {
        int piv = findpivot(nums);
        int n = nums.size();
        if(target >= nums[piv] && target <= nums[n - 1]){
            return bs(nums,piv,n-1,target);
        }
        else {
            return bs(nums,0,piv-1,target);
        }
    }
};
