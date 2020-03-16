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
