"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.helper(node)
            
    def helper(self, node, visited={}):
        if node in visited:
            return visited[node]
        if node:
            copy = Node(node.val, [])
            visited[node] = copy

            copy.neighbors = [self.helper(neighbor, visited) for neighbor in node.neighbors]

            return copy