function ListNode(val) {
  this.val = val;
  this.next = null;
}

function consoleList(list) {
  let outstr = '';
  while (list) {
    if (outstr) {
      outstr += ' -> ';
    }
    outstr += list.val;
    list = list.next;
  }
  console.log(outstr);
}

function createListNode(arrs) {
  let root = null;
  let index = null;
  for (let i = 0; i < arrs.length; i++) {
    if (!root) {
      root = new ListNode(arrs[i]);
      index = root;
    } else {
      index.next = new ListNode(arrs[i]);
      index = index.next;
    }
  }
  return root;
}

module.exports = {
  ListNode,
  consoleList,
  createListNode
};
