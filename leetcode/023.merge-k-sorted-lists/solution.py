'''
将每一个链表的节点加入到无序数组中进行排序，再重新构建新的链表。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        arrs = []
        for list in lists:
            while list:
                arrs.append(list.val)
                list = list.next
        arrs.sort()
        newListNode = newListArrow = None
        for item in arrs:
            if not newListNode:
                newListNode = ListNode(item)
                newListArrow = newListNode
            else:
                newListNode.next = ListNode(item)
                newListNode = newListNode.next
        return newListArrow
