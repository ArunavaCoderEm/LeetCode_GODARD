 

void rotate(int** matrix, int matrixSize, int* matrixColSize) {
    int i,j,tr[300][300];
    for (i = 0; i < matrixSize; ++i){
        for (j = 0; j < matrixSize; ++j){
            tr[i][j] = matrix[j][i];
        }
    }
    for (i = 0; i < matrixSize; ++i){
        for (j = 0; j < matrixSize; ++j){
            matrix[i][j] = tr[i][j];
        }
    } 
    for (int k = 0; k < matrixSize; ++k){
        int i1 = 0, j1 = matrixSize - 1,temp; 
        while (i1 < j1) { 
           temp = matrix[k][i1];
           matrix[k][i1] = matrix[k][j1];
           matrix[k][j1] = temp;
            i1++, j1--; 
        } 
    }
}