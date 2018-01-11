/**
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 *
 *
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const addTwoNumbers = (l1, l2) => {
  let addSum = l1.val + l2.val
  let sumNode = new ListNode(addSum % 10)
  let tmpNode = sumNode
  while (l1.next || l2.next || addSum > 9) {
    l1 = l1.next || new ListNode(0)
    l2 = l2.next || new ListNode(0)
    addSum = l1.val + l2.val + (addSum > 9 ? 1 : 0)
    tmpNode.next = new ListNode(addSum % 10)
    tmpNode = tmpNode.next
  }
  return sumNode
}

// Runtime: 236 ms, beats 32.24%
