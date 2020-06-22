function shallowClone(obj) {
  if (typeof obj !== 'object') return obj;
  const newObj = obj instanceof Array ? [] : {};
  for (let key of Object.keys(obj)) {
    newObj[key] = obj[key];
  }
  return newObj;
}
