# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        dummy = ListNode()
        dummy.next = head
        fast = head
        slow = head
        sever = dummy

        while fast and fast.next:
            sever = sever.next
            slow = slow.next
            fast = fast.next.next

        sever.next = None

        curr = slow
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        first = head
        second = prev
        curr = dummy
        
        while first or second:
            if first:
                curr.next = first
                curr = first
                first = first.next
            if second:
                curr.next = second
                curr = second
                second = second.next
            


            
            




