# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    '''
    这是一个比较笨的办法，保留头部指针，先将每个节点加上 prev 指针，再倒着进行查询替换
    '''
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        begin = ListNode(0)
        begin.next = head
        index = begin
        while index.next:
            index.next.prev = index
            index = index.next
        while n - 1 > 0:
            index = index.prev
            n -= 1
        index.prev.next = index.next
        return begin.next

    '''
    使用两个指针同时从头查到尾，其中一个延迟n步进行查找，则当一个指针查询到尾部时，另外一个指针则为倒数第n+1个数
    '''
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        begin = ListNode(0)
        begin.next = head
        start = begin
        end = begin
        offset = 0
        while end.next:
            offset += 1
            end = end.next
            if offset > n:
                start = start.next
        start.next = start.next.next
        return begin.next
        
        
