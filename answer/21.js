/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const mergeTwoLists = (l1, l2) => {
  let newNode = new ListNode(0)
  let returnNode = newNode
  let isEnd = false
  while (!isEnd) {
    if (!l1) {
      newNode.next = l2
      isEnd = true
    } else if (!l2) {
      newNode.next = l1
      isEnd = true
    } else {
      if (l1.val < l2.val) {
        newNode.next = new ListNode(l1.val)
        l1 = l1.next
      } else {
        newNode.next = new ListNode(l2.val)
        l2 = l2.next
      }
      newNode = newNode.next
    }
  }
  return returnNode.next
}

const mergeTwoLists_recursive = function(l1, l2) {
  if (!l1) return l2
  if (!l2) return l1
  if (l1.val < l2.val) {
    l1.next = mergeTwoLists(l1.next, l2)
    return l1
  } else {
    l2.next = mergeTwoLists(l1, l2.next)
    return l2
  }
}
