/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    var x = this.length - 1;
    if (x + 1 != 0){
        return this[x]
    }
    else {
        return -1;
    }
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */