class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map keys to nodes
        self.left, self.right = Node(0, 0), Node(0, 0) # Default values
        self.left.next, self.right.prev = self.right, self.left # point them to each other

    # remove node from the list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # insert node at right between prev
    # prev <--> prev <--- here ---> right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # Update most recent node
            self.remove(self.cache[key])
            self.insert(self.cache[key]) # Nodes on the right are not LRU

            return self.cache[key].val # Return the node's value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        # Create node
        self.cache[key] = Node(key, value)
        # Insert node on the right (NOT LRU)
        self.insert(self.cache[key])

        # If length of list exceeds capacity
        if len(self.cache) > self.cap:
            # Remove from list and delete the LRU from the hashmap
            lru = self.left.next # head of linked list
            self.remove(lru)
            del self.cache[lru.key]

