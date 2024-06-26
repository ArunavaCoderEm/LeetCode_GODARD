class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int s = 0, e = arr.size() - 1;
        int mid = (s + (e - s) / 2);
        while(s <= e) {
            // if peak
            if(arr[mid] > arr[mid + 1] && arr[mid] > arr[mid - 1]) return mid;
            // if not peak
            else if(arr[mid] < arr[mid + 1]) s = mid + 1;
            else e = mid - 1;
            mid = (s + (e - s) / 2);
        } 
        return mid;
    }
};
