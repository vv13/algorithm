String.prototype.reverse = function () {
  return String(this).split('').reverse().join('');
};

const a = 'abcd';
console.log(a.reverse());
