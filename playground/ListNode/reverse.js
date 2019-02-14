// 翻转链表

const executor = require('../executor');
const { createListNode, consoleList } = require('../base/ListNode');

consoleList();

const input = [createListNode([2, 3, 5, 7, 9, 11])];

function main(head) {
  let a = head;
  let b = head.next;
  let c = null;

  a.next = null;
  while (b) {
    c = b.next;
    b.next = a;

    a = b;
    b = c;
  }
  head = a
  consoleList(head)
}

executor(main, input, {});
