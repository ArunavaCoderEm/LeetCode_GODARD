/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int * productExceptSelf(int* nums, int n, int* r) {
    int i,j, *res,z = 0;
    res = (int*)malloc(n*sizeof(int));
    int mul = 1, muln = 1;
    for(int t = 0; t < n; ++t){
        res[t] = 0;
    }
    for(int i = 0; i < n; ++i){
        if(nums[i] == 0){ 
            z++;
        }
        mul *= nums[i];
        if(nums[i] != 0) muln *= nums[i];
    }
    if(z > 1){
        *r = n;
        return res;
    }
    if(z == 1){
        for(int h = 0; h < n; ++h){
            if(nums[h] != 0) res[h] = 0;
            else res[h] = muln;
        }
    }
    else {
        for(int j = 0; j < n; ++j){
                res[j] = mul / nums[j];
        }
    }
    *r = n;
    return res;
}