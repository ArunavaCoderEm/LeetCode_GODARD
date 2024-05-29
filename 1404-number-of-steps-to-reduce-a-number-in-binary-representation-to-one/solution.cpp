class Solution {
public:
    int numSteps(string s) {
       long long int num = stoi(s, nullptr, 2);
       int step = 0;
        while(num != 1){
            int rem = (num & 1);
            if(rem == 1) num++;
            else num = num >> 1;
            step++;
        } 
        return step;
    }
};
