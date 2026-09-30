# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the linked list is empty, return an empty linked list
        if not head:
            return head

        # If there is only one element, return only one element
        # On second thought, I don't think you need to check for this edge case.

        # Create two variables; current = head, and prev = none
        current = head
        prev = None

        # If there is more than one element in the linked list:
        # while current is not none:
        # Store the nextNode
        # Set current's next node to the previous node
        # Set the prev node to the current node
        # Iterate by setting current to nextNode
        while current is not None:
            nextNode = current.next
            if nextNode is None:
                head = current
            current.next = prev
            prev = current
            current = nextNode

        # Remember that we have to return the head of the linked list
        return head
