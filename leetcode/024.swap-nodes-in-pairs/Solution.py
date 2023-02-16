# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        arrow = ListNode(0)
        remain = arrow
        arrow.next = head
        while arrow.next and arrow.next.next:
            first = arrow.next
            second = arrow.next.next
            first.next = second.next
            second.next = first
            arrow.next = second
            arrow = arrow.next.next
        return remain.next
