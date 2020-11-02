# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        lo = hi = head
        while hi and hi.next:
            lo = lo.next
            hi = hi.next.next
            if lo == hi:
                break
        else:
            return None
        lo = head
        while lo != hi:
            lo = lo.next
            hi = hi.next
        return lo