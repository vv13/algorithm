function delay50Fail() {
  return new Promise((resolve, reject) => setTimeout(() => reject('err50'), 50));
}

function delay1000Success() {
  return new Promise((resolve, reject) => setTimeout(() => resolve('success1000'), 1000));
}

function waitForAll(...promises) {
  let count = 0;
  const max = promises.length;
  const resultArrs = new Array(max);
  return new Promise((resolve, reject) => {
    for (let i = 0; i < max; i++) {
      Promise.resolve(promises[i]).then(
        res => {
          resultArrs[i] = res;
          if (++count === max) {
            console.log('done');
            resolve(resultArrs);
          }
        },
        err => {
          resultArrs[i] = err;
          if (++count === max) {
            resolve(resultArrs);
          }
        }
      );
    }
  });
}

waitForAll(delay50Fail(), delay1000Success()).then(res => {
  console.log(res);
});
