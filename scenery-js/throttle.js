function throttle(func, timeframe) {
  let lastTime = 0;
  return function (...args) {
    const now = Date.now();
    if (now - lastTime >= timeframe) {
      func.apply(this, args);
      lastTime = now;
    }
  };
}

const throttler = throttle(console.log, 300);
throttler('hello1');
throttler('hello2');
setTimeout(() => {
  throttler('hello3');
}, 200);
setTimeout(() => {
  throttler('hello4');
}, 400);
