"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        hsh = {}
        hsh[node] = Node(node.val)
        q = deque([node])

        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in hsh:
                    hsh[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                hsh[curr].neighbors.append(hsh[neighbor])

        return hsh[node]    



