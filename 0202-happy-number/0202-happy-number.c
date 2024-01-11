int sq(int n){
    int rem = 0, summ = 0, temp = n;
    while (temp != 0){
        rem = temp % 10;
        summ += (rem*rem);
        temp /= 10;
    }
    return (summ);
}

bool isHappy(int n) {
    int res;
    do {
        res = sq(n);
        if(res == 1)
            return true;
        if (res == 4)
            return false;
        n = res;
    } while (res != 1 && res >= 1);
    return false;   
}