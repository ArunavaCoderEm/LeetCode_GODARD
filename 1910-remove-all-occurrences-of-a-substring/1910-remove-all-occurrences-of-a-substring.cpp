class Solution {
public:
string removeOccurrences(string s, string part)
{
    int pn = part.length();
    while (s.size() != 0 && s.find(part) < s.length()) {
        auto i = s.find(part);
        for (int k = 0; k < pn; ++k) {
            s.replace(i, 1, "");
        }
    }

    return s;

}
};