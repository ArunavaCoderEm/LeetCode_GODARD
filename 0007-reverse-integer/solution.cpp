class Solution {
public:
    int reverse(int x) {
        long long int res = 0, i = 0;
        while(x){
            long long int rem = x % 10;
            res = (10 * res) + rem;
            x /= 10;
        }   
        if(res >= INT_MAX || res <= INT_MIN){
            return 0;
        }
        return res;
    }
};
