type Fn = (...params: number[]) => number
// basically create a cache best optn object
function memoize(fn: Fn): Fn {
    let ob : any = {}
    return function(...args) {
        const res = JSON.stringify(args)
        if(res in ob) return ob[res] // ...args takes exist + new (if any)
        else {
            ob[res] = fn.apply(this,args) // if not in object add and ...args takes that
            return ob[res]
        }
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */