class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if(s.count('1') == 1):
            return True
        for i in range(len(s)-1):
            if(s[i] == '0'and s[i+1]  == '1'):
                return False
        return True

'''
bool checkOnesSegment(char* s) {
    int i, size = sizeof(s)/sizeof(char);
    for (i = 0; i < size; ++i){
        if (s[i] == '0' && s[i+1] == '1'){
            return false;
        }
    }
    return true;
}
'''