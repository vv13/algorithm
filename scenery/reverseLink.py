class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
