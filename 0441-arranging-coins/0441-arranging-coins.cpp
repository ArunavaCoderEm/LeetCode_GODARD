long long int helperSum (long long int x) {
    long long int res = (x * (x + 1)) / 2;
    return res;
}

// O(log(n)) Solution optimal ... this came to my dream ... I've become so bad at this
class Solution {
public:
  int arrangeCoins(int n) {
    long long int start = 1, end = n;
    if (n == 1) {
        return 1;
    }
    while (start <= end)
    {
        long long int mid = (start + (end - start) / 2);
        long long int currentSum = helperSum(mid);
        if (currentSum == n) {
            return mid; 
        }
        else if (currentSum > n)
        {
            end = mid - 1;
        }
        else
        {
            start = mid + 1;
        }
    }
    return end;
   }
};

// O(n) solution brute Forcce
// class Solution {
// public:
//     int arrangeCoins(int n) {
//         long long int i = 0, total = 0;
//         if (n == 0) {
//             return total;
//         }
//         while (total <= n) {
//             if (total + i <= n) {
//                 total += i;
//                 i++;
//             }
//             else break;
//         }
//         return i - 1;
//     }
// };
