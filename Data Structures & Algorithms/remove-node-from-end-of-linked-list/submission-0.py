# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reverse linked list
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        # Reverse the linked list again and remove the node (prev is new head)
        counter = 1
        while prev:
            if counter != n:
                temp = prev.next
                prev.next = head
                head = prev
                prev = temp
            else:
                prev = prev.next
                # Edge case, if removing last node:
                if prev is None:
                    return head
                temp = prev.next
                prev.next = head
                head = prev
                prev = temp

            counter += 1

            # let's say we want to remove the fourth node
            # Null <- 4 <- 3 <- 2 (head) <- 1 (prev) -> Null 
            # Null <- 4 <- 3 <- 2 (head) <- Null


        # Reverse linked list again
        
        return head