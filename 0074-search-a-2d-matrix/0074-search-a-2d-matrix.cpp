class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        int rows = matrix.size();
        int cols = matrix[0].size();

        int LinearTraverse = rows * cols;

        int start = 0, end = LinearTraverse - 1;

        if (rows == 1) {
            for (int i = 0; i < cols; ++i) {
                if (matrix[0][i] == target) return true;
            }
            return false;
        }

        while (start <= end) {

            int mid = (start + (end - start) / 2);

            int currElement = matrix[mid / cols][mid % cols];

            if (currElement == target) {
                return true;
            }

            if (currElement < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }

        }

        return false;

    }
};