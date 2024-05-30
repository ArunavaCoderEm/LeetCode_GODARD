class Solution {
public:
    // brute force exactly what the qstn said
    int countTriplets(vector<int>& arr) {
        int i,j,k,count = 0;
        for(i = 0; i < arr.size(); ++i){
            for(j = i + 1; j < arr.size(); ++j){
                int a = 0;
                for(k = i; k <= j-1; ++k){
                    a ^= arr[k];
                }                
            int b = 0;
            for(k = j; k < arr.size(); ++k){
                b ^= arr[k];
                if(a == b) count++;
            }
            }
        }
        return count;
    }
};