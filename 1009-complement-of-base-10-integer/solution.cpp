class Solution {
public:
    int bitwiseComplement(int n) {
        if(n == 0) return 1;
        int t = log2(n) + 1;
        int y = pow(2,t) - 1;
        return n ^ y;
    }
};
