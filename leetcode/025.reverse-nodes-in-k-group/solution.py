'''
分为两步：
1. 找到 k 位置，并给节点加上prev 指针
2. 翻转前部分链表
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseLink(node: ListNode) -> ListNode:
            first = node
            second = node.next
            first.next = None

            while first and second:
                next = second.next
                second.next = first

                first = second
                second = next
            return first

        def lenOfListNode(node: ListNode):
            n = 0
            while node:
                node = node.next
                n += 1
            return n


        len = lenOfListNode(head)
        new_node = ListNode(0)
        tail_new_node = new_node

        for _ in range(len // k):
            reverse_head = head
            # 找到交界处
            for i in range(k - 1):
                head = head.next

            tail = head.next
            head.next = None
            append_node = reverseLink(reverse_head)

            # 将翻转的指针添加进新的队列
            while append_node:
                tail_new_node.next = append_node
                tail_new_node = tail_new_node.next
                append_node = append_node.next

            head = tail
        tail_new_node.next = head

        return new_node.next
