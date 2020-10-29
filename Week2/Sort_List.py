# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
    
        if head:
            node = head
            values = []
            while True:
                values.append(node.val)
                node = node.next
                if not node:
                    break

            it = iter(sorted(values))
            root = node = ListNode(next(it))
            for value in it:
                node.next = ListNode(value)
                node = node.next
            return root