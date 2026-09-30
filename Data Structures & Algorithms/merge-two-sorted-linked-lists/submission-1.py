# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Questions:
# 1. Can there be negative numbers?
# 2. Will the sorted lists be the same length?
# 3. Do both lists' nodes start at the head?
# Both of which I answered just by reading the problem lol

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        # Create a dummy head node so we don't insert into an empty list
        dummy = ListNode()
        tail = dummy

        while (list1 and list2):
            if list1.val < list2.val: # list1 wins
                tail.next = list1
                list1 = list1.next
            else: # list2 wins
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next

        # What if one of them is shorter/empty now?
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # Return the actual list (dummy is not the actual head)
        return dummy.next
