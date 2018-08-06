/*

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

*/

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
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
