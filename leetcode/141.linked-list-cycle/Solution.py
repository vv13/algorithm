# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 记录每一个节点是否出现过
    def hasCycle(self, head: ListNode) -> bool:
        obj = set()
        while head:
            if head in obj:
                return True
            obj.add(head)
            head = head.next
        return False

    # 使用快慢指针的解法
    def hasCycle1(self, head: ListNode) -> bool:
        slow = fast = head
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True

        return False
