/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
    x = Math.sqrt(num);
    if(Number.isInteger(x)){
        return true
    }
    return false
};