/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    let x = Math.log(n) / Math.log(4);
    if(Number.isInteger(x)){
        return true;
    } 
    return false
};