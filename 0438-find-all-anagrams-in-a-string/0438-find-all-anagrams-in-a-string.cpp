class Solution {
    private:
        bool EqualConstantArrayChars(array<int, 26>& arr1, array<int, 26>& arr2) {
            for (int i = 0; i < 26; ++i) {
                if (arr1[i] != arr2[i]) return false;
            }
            return true;
        }
    public:
        vector<int> findAnagrams(string s, string p) {

            vector <int> res;
            array<int, 26> p_count = {0};
            int ss = s.size();
            int ps = p.size();

            if (ss < ps) return res;
            
            for (int i = 0; i < ps; ++i) {
                int eval = p[i] - 'a';
                p_count[eval]++;
            }

            int start = 0;
            array<int, 26> s_count = {0};
            
            while (start <= ss - ps) {
                int end = start;
                s_count.fill(0); 

                while (end < start + ps) {
                    int evalRe = s[end] - 'a';
                    s_count[evalRe]++;
                    end++;
                }

                if (EqualConstantArrayChars(s_count, p_count)) {
                    res.push_back(start);
                }

                start++;
            }

            return res;
        }
};