# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers method, N nodes between L and R node
        # When R node is Null, we know L will be at the Nth node from the end
        dummyNode = ListNode(0, head) # set dummyNode.next = head
        left = dummyNode
        right = head
    
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next

        # Now that left is before the node we want to remove...
        # Skip over the node we want to delete!
        # N = 3
        # 1 -> 2 (L) -> 3 -> 4 -> 5 -> Null (R)
        # 1 -> 2 (L) -> 4 -> 5 -> Null (R)
        left.next = left.next.next

        return dummyNode.next