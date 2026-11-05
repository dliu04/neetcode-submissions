# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: # If empty list
            return None

        while len(lists) > 1: # Keep reducing until there is only one list left
            mergedLists = []

            for i in range(0, len(lists), 2): # Increment by 2 each time
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None # Make sure not out of bounds
                mergedLists.append(self.mergeList(l1, l2))
            
            lists = mergedLists

        return lists[0]


    def mergeList(self, l1, l2):
        #TODO
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        # If leftover
        if l1:
            tail.next = l1
        if l2: 
            tail.next = l2
        
        return dummy.next
