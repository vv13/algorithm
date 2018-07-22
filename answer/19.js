/**
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 * 
Version1
var removeNthFromEnd = function(head, n) {
    const list = head
    while (head.next) {
        head.next.prev = head
        head = head.next
    }
    for (let i = 0; i < n - 1; i+= 1) {
        head = head.prev
    }
    head.prev.next = head.next
    return list
};
 *
 *
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
  const fake = new ListNode(-1)
  fake.next = head
  let start = fake
  let end = fake
  let count = 0
  while (end.next) {
    count += 1
    end = end.next
    if (count > n) {
      start = start.next
    }
  }
  start.next = start.next.next
  return fake.next
}
