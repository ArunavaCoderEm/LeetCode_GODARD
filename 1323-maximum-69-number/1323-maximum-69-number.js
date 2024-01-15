/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number  = function(num) {
    var x = String(num).split("")
    for (var i = 0; i < x.length; ++i){
        if (x[i] != "9"){
            x[i] = "9"
            return parseInt(x.join(""))
        }
    }
    return num
};