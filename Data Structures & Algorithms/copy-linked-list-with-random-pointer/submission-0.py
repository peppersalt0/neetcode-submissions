"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hsh = {}
        dummy = Node(0)
        prev = dummy
        curr = head

        while curr:
            copy = Node(curr.val)
            hsh[curr] = copy
            prev.next = copy
            prev = copy
            curr = curr.next
        
        curr = head
        copy = dummy.next
        while curr:
            copy.random = hsh[curr.random] if curr.random else None
            curr = curr.next
            copy = copy.next

        return dummy.next


