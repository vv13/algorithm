from ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = l = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, digit = divmod(sum, 10)
            l.next = ListNode(digit)
            l = l.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return l3.next
