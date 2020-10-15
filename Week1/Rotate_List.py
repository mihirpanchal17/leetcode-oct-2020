class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        node = head
        length = 1
        nodes_dict = {1:node}
        while node.next:
            length += 1
            node = node.next
            nodes_dict[length] = node
            
        k = k % length
        nodes_dict[length].next = head
        head = nodes_dict[length-k].next
        nodes_dict[length-k].next = None
        
        return head