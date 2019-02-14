/*
二分查找，查找指定输入数，发挥索引
*/
const executor = require('../executor');

const input = [[1, 3, 6, 9, 22, 23, 25], 25];

function main(arrs, key) {
  // const result = binarySearch(arrs, 0, arrs.length - 1, key);
  const result = binarySearchWhile(arrs, key);
  console.log(result);
}

// 递归
function binarySearch(arrs, start, end, key) {
  const middle = Math.floor((start + end) / 2);
  if (arrs[middle] === key) {
    return middle;
  } else if (arrs[middle] < key) {
    return binarySearch(arrs, middle + 1, end, key);
  } else {
    return binarySearch(arrs, start, middle - 1, key);
  }
}

// while
function binarySearchWhile(arrs, key) {
  let start = 0;
  let end = arrs.length - 1;
  while (start <= end) {
    const mid = start + (end - start) / 2
    if (arrs[mid] < key) {
      start = mid + 1
    } else if (arrs[mid] > key) {
      end = mid - 1
    } else {
      return mid
    }
  }
}

executor(main, input);
