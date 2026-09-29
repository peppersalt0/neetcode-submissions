# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        def remove(i):
            prev = dummy
            curr = head

            for _ in range(i):
                prev = prev.next
                curr = curr.next
            
            prev.next = curr.next
        
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        
        remove(count - n)
        return dummy.next



        