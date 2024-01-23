class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums
'''
OR YOU CAN USE THIS IN C

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

void merge (int arr[], int low, int mid, int high){
    int  i = low, j = mid + 1, k = low, A[high+low+1];
    while(i <= mid && j <= high){
        if(arr[i] > arr[j]){
            A[k] = arr[j];j++;k++;
        }
        else {
            A[k] = arr[i];i++;k++;
        }
    }
    while(i <= mid){
        A[k] = arr[i];i++;k++;
    }
    while (j <= high){
        A[k] = arr[j];k++;j++;
    }
    for (int t = 0; t <= high; ++t){
        arr[t] = A[t];
    }
}

void mergesort(int arr[], int low, int high){
    if(low < high){
        int mid = (low + high)/2;
        mergesort(arr,low,mid);
        mergesort(arr,mid+1,high);
        merge(arr,low,mid,high);
    }
}

int* sortArray(int* nums, int numsSize, int* returnSize) {
    mergesort(nums,0,numsSize-1);
    return nums;
}
'''
