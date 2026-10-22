# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the half using fast and slow pointer
        slow, fast = head, head
        # By the time fast is null, slow is at halfway point
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        # Split the list in half
        secondHalfHead = slow.next
        slow.next = None
        prevNode = None

        # Reverse the second half
        while secondHalfHead:
            nextNode = secondHalfHead.next
            secondHalfHead.next = prevNode
            prevNode = secondHalfHead
            secondHalfHead = nextNode

        # Start with first half, assign second half nodes between
        # first half nodes
        first = head
        second = prevNode # head of the reversed second half

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
