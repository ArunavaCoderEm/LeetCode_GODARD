type Fn = (...params: any[]) => Promise<any>;

function timeLimit(fn: Fn, t: number): Fn {
    // easy just create a callback that takes within setTimeout
    // spreaded rest args and try to resolve
    // if cant within time then reject with error
    return async function(...args) {
        return new Promise((resolve, reject) => {
            setTimeout(() => reject("Time Limit Exceeded"), t);
            fn(...args).then(resolve, reject);
        });
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */