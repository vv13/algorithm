const main = require('./main');

const input = [[3, 5, 7, 8, 9], [2, 4, 5, 8]];

main(combine, input);
main(combine1, input);

// 随手写的函数
function combine(arr1, arr2) {
  const newarrs = [];
  let arr1Index = 0;
  let arr2Index = 0;
  const len = arr1.length + arr2.length;
  for (let i = 0; i < len; i++) {
    if (arr1Index === arr1.length) {
      for (let left = arr2Index; left < arr2.length; left++) {
        newarrs.push(arr2[left]);
        arr2Index++;
      }
    } else if (arr2Index === arr2.length) {
      for (let left = arr1Index; left < arr1.length; left++) {
        newarrs.push(arr1[left]);
        arr1Index++;
      }
    } else {
      if (arr1[arr1Index] < arr2[arr2Index]) {
        newarrs.push(arr1[arr1Index++]);
      } else {
        newarrs.push(arr2[arr2Index++]);
      }
    }
  }
  return newarrs;
}

/**
 * 以第一个数组为基准，不用浪费空间
 * 倒序开始修改，不用频繁修改索引
 * @param {*} arr1
 * @param {*} arr2
 */
function combine1(arr1, arr2) {
  let index = arr1.length + arr2.length - 1;
  let arr1Index = arr1.length - 1;
  let arr2Index = arr2.length - 1;

  while (index >= 0) {
    if (arr1Index < 0) {
      for (; arr2Index >= 0; arr2Index--) {
        arr1[index] = arr2[arr2Index];
      }
      break;
    } else if (arr2Index < 0) {
      break;
    } else {
      if (arr1[arr1Index] > arr2[arr2Index]) {
        arr1[index] = arr1[arr1Index--];
        index--;
      } else {
        arr1[index] = arr2[arr2Index--];
        index--;
      }
    }
  }
  return arr1
}
