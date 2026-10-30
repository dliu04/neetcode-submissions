# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Assuming that l1 and l2 are both heads

        dummy = ListNode(0)
        sum = ListNode(0)
        dummy.next = sum

        while l1 is not None or l2 is not None:
            # Add two values together to produce a nodeSum
            if l1 is not None and l2 is not None:
                nodeSum = l1.val + l2.val
            elif l1 is not None:
                nodeSum = l1.val
            elif l2 is not None:
                nodeSum = l2.val

            # add nodeSum by 1 if there was a carryover
            if sum.val != 0:
                nodeSum = nodeSum + sum.val
            
            # if it's over 10, calculate the remainder and set it to current value
            # Since it cannot be over 19 (single digit addition)...
            # create a new node to preserve carryover
            # if nodeSum over 10, set newNode.val(1)
            if nodeSum >= 10:
                sum.val = nodeSum - 10
                sum.next = ListNode(1, None)
            else: # If it is less than 10, just assign to sum.val and move on
                sum.val = nodeSum
                sum.next = ListNode(0, None)

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            sum = sum.next
        
        # If a 0 is at the end, remove it.
        # Destroy node at the end of the list
        if sum.val == 0:
            curr = dummy.next
            while curr.next.next is not None:
                curr = curr.next
            
            curr.next = None

        return dummy.next

        # l1=[9,9,9,9,9,9,9]
        # l2=[9,9,9,9]
        # 8 9 9 9 1