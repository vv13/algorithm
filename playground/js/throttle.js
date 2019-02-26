function throttle(fn, delay) {
  let lock = false;
  
  return (...args) => {
      if (lock) return;
      lock = true;
      setTimeout(() => {
          lock = false;
          fn(args)
      }, delay)
  }    
}
