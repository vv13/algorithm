/*
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
*/
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
  if (!head || !head.next) return head;
  let prev = null
  let index = head
  let next = head.next
  let firstHead = next ? null : index
  
  while(index && next) {
      const _index = index;
      const _next = next;
      
      const next2 = _next.next
      
      if (prev) {
          prev.next = _next;
      }

      _next.next = _index;
      _index.next = next2;
      
      if (!firstHead) {
          firstHead = _next
      }
      
      prev = _index
      index= _index.next
      next = index ? _index.next.next : null
  }
  return firstHead;
};
