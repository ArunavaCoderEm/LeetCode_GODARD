class Solution {
public:
    void rotate(vector<int> &v, int k) {
        
        int n = v.size();
        int actualRotations = k % n;

        if (actualRotations == 0) {
            return;
        }

        vector <int> temp;

        for (int i = (n - actualRotations); i < n; ++i) {
            temp.push_back(v[i]);
        }

        int counter = 0;
        for (int j = n - actualRotations - 1; j >= 0; --j) {
            v[n - 1 - counter++] = v[j];
        }

        for (int k = 0; k < actualRotations; ++k) {
            v[k] = temp[k];
        }
    }
};
