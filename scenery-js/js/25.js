/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
  if (k <= 1) return head;

  // save head
  const _head = head;
  
  // add prev
  while(head.next) {
      head.next.prev = head;
      head = head.next;
  }
  
  // start reverse index with first node
  let next = hasNext(_head, k)
  while(next) {
      const _next = next.next
      for (let i = 0; i < k; i++) {
          next.next = next.prev;
          next = next.prev;
      }
      if (next) {
          next.next = _next;
          next = hasNext(next.next, k);
      }
  }
  
  return _head;
  while(continueNode) {
      const reverseNode = getReverseNode(continueNode, _head)
      console.log(_head.next, reverseNode)
      continueNode = canContinue(reverseNode, k)
  }
  return _head.next
};

// check enough
function hasNext(node, k) {
  for (let i = 0; i < (k - 1); i += 1) {
      if (!node.next) {
          return false
      }
      node = node.next
  }
  return node;
}
