# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # use a k pointer
        # use a dummy node since we are changing head
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kthNode = self.getKth(groupPrev, k)
            if not kthNode: # if at the end of list
                break
            
            groupNext = kthNode.next

            # reverse the group
            prev, curr = kthNode.next, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            temp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = temp
        
        return dummy.next


    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr