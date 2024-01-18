/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    res = new Set(nums);
    var start = 1;
    while(res.has(start)){
        start++;
    }
    return start;
};