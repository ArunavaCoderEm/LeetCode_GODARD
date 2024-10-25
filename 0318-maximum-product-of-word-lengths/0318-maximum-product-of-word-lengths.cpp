// THIS IS WHAT I CALL A GOOD QUESTION FOR OPTIMIZATION
// CONCEPTS OF LOOKUP TIME IN SETS, DAMN !!!

bool haveCommonLetters(const unordered_set<char>& set1, const unordered_set<char>& set2) {

    for (char ch : set1) {

        if (set2.count(ch)) { 

            return true;

        }
    }

    return false;
}

class Solution {
public:
    int maxProduct(vector<string>& words) {

        int n = words.size();
        int maxProd = 0;

        vector<int> lengths(n);
        vector<unordered_set<char>> charSets(n);

        for (int i = 0; i < n; ++i) {

            lengths[i] = words[i].length();
            charSets[i] = unordered_set<char>(words[i].begin(), words[i].end());

        }

        int i = 0, j = 1;

        while (i < n) {
            if (j < n) {
                int prod = lengths[i] * lengths[j];
                
                if (prod > maxProd && ! haveCommonLetters(charSets[i], charSets[j])) {
                    maxProd = prod;
                }
            }

            j++;
            if (j >= n) {
                i++;
                j = i + 1;
            }
        }

        return maxProd;
    }
};