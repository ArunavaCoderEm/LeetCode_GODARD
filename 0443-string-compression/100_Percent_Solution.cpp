class Solution {
public:
    int compress(vector<char>& chars) {
        
        int currIndex = 0;
        int n = chars.size();
        int i = 0;

        while (i < n) {

            int j = i + 1;

            while (j < n && chars[i] == chars[j]) {
                j++;
            }

            int count = (int) (j - i);

            if (count > 1) {

                chars[currIndex++] = chars[i];
                
                if (count >= 10) {

                    string newC = to_string(count);
                    for (char ch: newC) {
                        chars[currIndex++] = ch;
                    }

                } else {
                    
                    string resC = to_string(count);
                    chars[currIndex++] = resC[0];

                }

            } else {

                chars[currIndex++] = chars[i];

            }

            i = j;

        }

        return currIndex;

    }
};
