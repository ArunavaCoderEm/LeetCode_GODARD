class Solution {
private:
    int prod (int n) {
        int p = 1;

        while (n != 0) {

            int rem = n % 10;
            p = p * rem;
            n = n / 10;

        }
        
        return p;

    }
public:
    int smallestNumber(int n, int t) {
        int temp = n;
        while (true) {
            int p = prod(temp);
            if (p % t == 0) {
                return temp;
            }
            temp++;
        }
    }
};