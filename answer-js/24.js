/*
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

/*
Version 2:
  相比较于v1，v2不再维护交换数的索引prev index nextd，因为索引交换后，再将索引进行赋值，逻辑比较复杂，因此只需要记录当前指针的位置，然后取当前指针的后两位数进行判断即可。
*/
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
