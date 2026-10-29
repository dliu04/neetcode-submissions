"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = { None: None } # Edge case for null value

        # oldToCopy
        # Key: original node, value: copied node

        cur = head
        while cur:
            copy = Node(cur.val) # Create a copy of the node with the value
            oldToCopy[cur] = copy # Store it in the hash map
            cur = cur.next
        

        cur = head
        while cur:
            copy = oldToCopy[cur] # Retrieve copied node
            copy.next = oldToCopy[cur.next] # Assign it its pointers
            copy.random = oldToCopy[cur.random] 
            cur = cur.next
        
        return oldToCopy[head]