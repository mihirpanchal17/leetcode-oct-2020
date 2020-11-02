# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        q=[(root,1)]
        while q:
            node,n=q.pop(0)
            if not node.left and not node.right:
                return n
            if node.left:
                q.append((node.left,n+1))
            if node.right:
                q.append((node.right,n+1))