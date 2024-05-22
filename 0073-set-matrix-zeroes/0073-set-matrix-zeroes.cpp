class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();
        int r[201] = {0};
        int c[201] = {0};
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                if(matrix[i][j] == 0){
                    r[i] = -1; c[j] = -1;
                }
            }
        }
        for(int k = 0; k < n; ++k){
            for(int b = 0; b < m; ++b){
                if(r[k] == -1 || c[b] == -1){
                    matrix[k][b] = 0;
                }
            }
        }      
    }
};


// class Solution:
//     def setZeroes(self, matrix: List[List[int]]) -> None:
//         n = len(matrix)
//         m = len(matrix[0])
//         r = [0]*n
//         c = [0]*m
//         for i in range(0,n):
//             for j in range(0,m):
//                 if(matrix[i][j] == 0):
//                     r[i] = 1
//                     c[j] = 1
        
//         for i in range(0,n):
//             for j in range(0,m):
//                 if(r[i] or c[j]):
//                     matrix[i][j] == 0