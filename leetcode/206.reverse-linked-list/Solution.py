# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        new_head = None
        while cur:
            next = cur.next # backup next node
            cur.next = new_head
            new_head = cur
            cur = next
        return new_head

        