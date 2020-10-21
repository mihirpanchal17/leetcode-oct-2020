# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        order = []
        def preorder(root):
            if root:
                order.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return " ".join(map(str,order))
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        values = collections.deque(map(int,data.split()))
        def tree(min_val,max_val):
            if values and min_val < values[0] <= max_val:
                value = values.popleft()
                node = TreeNode(value)
                node.left = tree(min_val,value)
                node.right = tree(value,max_val)
                return node
            
        return tree(float("-inf"),float("inf"))