/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
  let newNode = null;
  let newNodeArrow = null;
  const listsArrs = [];
  lists.forEach(list => {
    listsArrs.push(list.val);
    while (list.next) {
      list = list.next;
      listsArrs.push(list.val);
    }
  });
  for (let i = 0; i < listsArrs.length; i++) {
    for (let j = i + 1; j < listsArrs.length; j++) {
      if (listsArrs[i] > listsArrs[j]) {
        const tmp = listsArrs[i];
        listsArrs[i] = listsArrs[j];
        listsArrs[j] = tmp;
      }
    }
    if (newNode) {
      newNodeArrow.next = new ListNode(listsArrs[i]);
      newNodeArrow = newNodeArrow.next;
    } else {
      newNode = new ListNode(listsArrs[i]);
      newNodeArrow = newNode;
    }
  }
  return newNode;
};
