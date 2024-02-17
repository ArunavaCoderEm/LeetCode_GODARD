bool increasingTriplet(int* nums, int numsSize) {
    int left = INT_MAX, right = INT_MAX;
    int i;
    for(i = 0; i < numsSize; ++i){
        if(nums[i] <= left){
            left = nums[i];
        }
        else if(nums[i] <= right){
            right = nums[i];
        }
        else{
            return true;
        }
    }
    return false;
}