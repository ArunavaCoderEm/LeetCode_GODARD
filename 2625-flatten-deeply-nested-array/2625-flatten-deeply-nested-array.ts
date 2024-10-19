type MultiDimensionalArray = (number | MultiDimensionalArray)[];

// now this is what I call a good question 
// I'm just loving typescript
// best uses of spread and reduce operator

var flat = function (arr:  MultiDimensionalArray, n: number):  MultiDimensionalArray {
    if (n < 1) return arr;
    return arr.reduce<MultiDimensionalArray>((accu, value) => {
        if(Array.isArray(value)) {
            accu.push(...flat(value, n-1));
        } else {
            accu.push(value);
        }
        return accu;
    }, [])
};