
function deepCopySimple(obj) {
  return JSON.parse(JSON.stringify(obj));
}

function deepClone(obj) {
  if (typeof obj !== 'object') return obj;
  const newObj = obj instanceof Array ? [] : {};
  for (let key of Object.keys(obj)) {
    if (typeof obj[key] !== 'object') {
      newObj[key] = obj[key];
    } else {
      newObj[key] = deepClone(obj[key]);
    }
  }
  return newObj;
}
