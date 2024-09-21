// back in the game bi***

void helperDfs (vector<int> &result, int n, int currentEval) {
    if (currentEval > n) {
        return;
    }
    result.push_back(currentEval);
    for (int i = 0; i <= 9; ++i) {
        long int temp = (10 * currentEval + i);
        if (temp > n) {
            return;
        }
        helperDfs(result, n, temp);
    }
}


class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> lex_answer;
        for (int i = 1; i <= 9; ++i) {
            helperDfs(lex_answer, n, i);
        }
        return lex_answer;
    }
};