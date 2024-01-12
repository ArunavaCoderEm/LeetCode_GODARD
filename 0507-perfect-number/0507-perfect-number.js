/**
 * @param {number} num
 * @return {boolean}
 */
var checkPerfectNumber = function(num) {
    var sum = 0;
    for (var i = 1; i <= num/2; ++i){
        if (num % i == 0){
            sum += i;
        }
    }
    return sum == num;
};