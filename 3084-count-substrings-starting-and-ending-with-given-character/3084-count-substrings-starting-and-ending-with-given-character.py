# class Solution:
#     def countSubstrings(self, s: str, c: str) -> int:
        # i = 0
        # count = 0
        # j = i + 1
        # while(i < len(s)):
        #     if(s[i:j].startswith(c) and s[i:j].endswith(c)):
        #         j += 1
        #         count += 1
        #     else:
        #         j += 1
        #     if(j > len(s)):
        #         i += 1
        #         j = i + 1
        # return count        

class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        co = 0
        for i in range(0,len(s)):
            if(s[i] == c): co += 1
        res = co*(co + 1)//2
        return res

'''  C code
long long countSubstrings(char* s, char c) {
    long long co = 0;
    for(long long k = 0; k < strlen(s); k++){
        if(s[k] == c) co++;
    }
    long long int res = (co*(co+1)) / 2;
    return res;
}
'''