function debounce(fn, delay) {
  let timerId = null;
  
  return (...args) => {
      if (timerId) {
          clearTimeout(timerId);
          timerId = null;
      }
      timerId = setTimeout(() => {
          timerId = null;
          fn(args)
      }, delay)
  }    
}
