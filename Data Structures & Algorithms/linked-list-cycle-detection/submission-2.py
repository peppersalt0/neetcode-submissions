# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            one = head
            two = head
        else:
            return False
        
        while two.next and two.next.next:
            one = one.next
            two = two.next.next

            if one.val == two.val:
                return True
        
        return False