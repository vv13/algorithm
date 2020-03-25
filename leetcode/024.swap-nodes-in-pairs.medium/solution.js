var swapPairs = function(head) {
  if (!head || !head.next) return head;
  const firstHead = new ListNode(0)
  firstHead.next = head;

  let index = firstHead
  
  while(index.next && index.next.next) {
      const first = index.next;
      const second = index.next.next;
      first.next = second.next
      index.next = second;
      index.next.next = first;
      index = index.next.next
  }
  return firstHead.next;
};
