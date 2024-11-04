class Solution {
private:
    bool EqualConstantArrayChars(array<int, 26>& arr1, array<int, 26>& arr2) {
        for (int i = 0; i < 26; ++i) {
            if (arr1[i] != arr2[i]) return false;
        }
        return true;
    }
public:
    bool checkInclusion(string s1, string s2) {
        array<int, 26> s1_count = {0};
        int s1s = s1.size();

        if (s1s > s2.size()) return false;
        
        for (int i = 0; i < s1s; ++i) {
            int eval = s1[i] - 'a';
            s1_count[eval]++;
        }

        int start = 0;
        array<int, 26> s2_count = {0};
        
        while (start <= s2.length() - s1s) {
            int end = start;
            s2_count.fill(0); 

            while (end < start + s1s) {
                int evalRe = s2[end] - 'a';
                s2_count[evalRe]++;
                end++;
            }

            if (EqualConstantArrayChars(s1_count, s2_count)) {
                return true;
            }

            start++;
        }

        return false;
    }
};

// import itertools
// class Solution:
//     def checkInclusion(self, s1: str, s2: str) -> bool:
//         perm = itertools.permutations(s1)
//         perms = [''.join(p) for p in perm]
//         for per in perms:
//             if(per in s2): return True
//         return False

// class Solution:
//     def checkInclusion(self, s1: str, s2: str) -> bool:
        
//         c = Counter(s1)

//         n, m = len(s1), len(s2)

//         i = 0
//         j = i + n

//         while (i < m) :
//             sub_c = Counter(s2[i:j])
//             if(sub_c == c) : return True
//             i += 1
//             j = i + n

//         return False
