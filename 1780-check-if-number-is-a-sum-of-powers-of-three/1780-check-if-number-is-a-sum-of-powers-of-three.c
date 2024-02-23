bool checkPowersOfThree(int n) {
    for(int i = 15; i >= 0; i--){
        int res = pow(3,i);
        if(res <= n){
            n -= res;
        }
        if(n == 0){
            return true;
        }
    }
    return false;
}