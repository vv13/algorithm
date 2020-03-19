function curry(fn) {
  const curryHelper = (currentArgs, fn) => (...args) => {
    const newArgs = currentArgs.concat(args);
    if (newArgs.length === fn.length) {
      fn.apply(this, newArgs);
    } else {
      return curryHelper(newArgs, fn);
    }
  };
  return curryHelper([], fn);
}

function doSomething(a, b, c) {
  console.log(a, b, c);
}

const curried = curry(doSomething);
curried(1, 2, 3);
curried(1)(2, 3);
curried(1)(2)(3);
