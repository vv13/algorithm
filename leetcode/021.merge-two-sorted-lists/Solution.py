# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        index = head
        while l1 or l2:
            if not l1:
                index.next = l2
                l2 = None
            elif not l2:
                index.next = l1
                l1 = None
            else:
                if l1.val < l2.val:
                    index.next = ListNode(l1.val)
                    index = index.next
                    l1 = l1.next
                else:
                    index.next = ListNode(l2.val)
                    index = index.next
                    l2 = l2.next
        return head.next
