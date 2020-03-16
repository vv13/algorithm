/**
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
