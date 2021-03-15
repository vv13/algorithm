function debounce(func, delay) {
  let timeout = null;
  return function (...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => {
      func.apply(this, args);
      timeout = null;
    }, delay);
  };
}

const debouncer = debounce(console.log, 300);
debouncer('hello1');
debouncer('hello2');
setTimeout(() => {
  debouncer('hello3');
}, 200);
setTimeout(() => {
  debouncer('hello4');
}, 400);
