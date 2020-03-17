'''
这是一个比较笨的办法，保留头部指针，先将每个节点加上 prev 指针，再倒着进行查询替换
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        begin = ListNode(0)
        begin.next = head
        index =begin 
        while index.next:
            index.next.prev = index
            index = index.next
        while n - 1 > 0:
            index = index.prev
            n -= 1
        index.prev.next = index.next
        return begin.next

        
        