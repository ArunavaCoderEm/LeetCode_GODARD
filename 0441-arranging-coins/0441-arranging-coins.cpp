class Solution {
public:
    int arrangeCoins(int n) {
        long long int i = 0, total = 0;
        if (n == 0) {
            return total;
        }
        while (total <= n) {
            if (total + i <= n) {
                total += i;
                i++;
            }
            else break;
        }
        return i - 1;
    }
};