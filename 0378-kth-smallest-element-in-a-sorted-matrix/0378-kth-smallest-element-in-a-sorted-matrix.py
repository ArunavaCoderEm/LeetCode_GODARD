class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                res.append(matrix[i][j])
        res.sort()
        return res[k-1]

''' C
void merge(int arr[],int low,int mid,int high){
    int i = low, j = mid + 1, k = low, a[2000];
    while(i <= mid && j <= high){
        if(arr[i] > arr[j]){
            a[k++] = arr[j++];
        }
        else{
            a[k++] = arr[i++];
        }
    }
    while(i <= mid){
        a[k++] = arr[i++];
    }
    while(j <= high){
        a[k++] = arr[j++];
    }
    for(int t = 0; t <= high; ++t){
        arr[t] = a[t];
    }
}
void merges(int arr[],int low,int high){
    if(low < high){
        int mid = (low + high) / 2;
        merges(arr,low,mid);
        merges(arr,mid+1,high);
        merge(arr,low,mid,high);
    }
}
int kthSmallest(int** matrix, int matrixSize, int* matrixColSize, int k) {
    int arr[2000],r=0;
    for (int i = 0; i < matrixSize; ++i){
        for (int j = 0; j < matrixSize; ++j){
            arr[r++] = matrix[i][j];
        }
    }
    int s = sizeof(arr)/sizeof(arr[0]);
    merges(arr,0,s-1);
    return arr[r-1];
}
'''