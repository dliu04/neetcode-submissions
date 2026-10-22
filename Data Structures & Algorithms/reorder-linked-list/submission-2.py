# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Set second half head
        second = slow.next
        prev = slow.next = None

        # Reverse second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Merge two halves
        first = head
        second = prev # second is null, but prev is right before null 

        # We know second list could be shorter
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2