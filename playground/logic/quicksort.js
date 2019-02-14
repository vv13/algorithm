// 快速排序
function quicksort(arrs, left, right) {
  if (left > right || left < 0 || right < 0) return;
  const middle = arrs[left];
  let low = left;
  let high = right;
  while (low < high) {
    while (low < high && arrs[high] >= middle) {
      high--;
    }
    arrs[low] = arrs[high];
    while (low < high && arrs[low] <= middle) {
      low++;
    }
    arrs[high] = arrs[low];
  }
  arrs[low] = middle;
  sort(arrs, left, low - 1);
  sort(arrs, low + 1, right);
  return arrs
}

const result = sort([5,3,9,7,10,3,1], 0, 6);
console.log(result)
