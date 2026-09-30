# We have to create a hashmap of key, value pairs
# the "value" here is going to have a [val, timestamp] format
# So something like this: key = value, timestamp

# The goal is to be able to set and get values
# Set is straightforward enough. We can append to the corresponding key
# in O(1) time

# Getting, however, might be tricky. If we are trying to retrieve a value of a key
# and we provide it with a timestamp that has not yet occurred (e.g getting a timestamp
# of 5 even though the most recent was 3 for a specific key) might force us to perform
# a binary search on that key's timestamps. 

# That's why the timestamps were already presorted for us.

class TimeMap:

    def __init__(self):
        # Constructor
        self.store = {} # key=string, value=[list of [val, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
            # Note: you CAN use a defaultdict to init keys if it doesn't
            # already exist, but that's an easy way out.
            # Let's challenge ourselves!
        
        # Append a value to the end of the list
        # In this case, our value is yet another list. We are
        # appending a list to the end of a list.
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        result = ""
        # The get operation: if we find a match, it will return that list
        # If the key is foo, then the .get method will return the list of pairs
        # associated with foo
        # The [] is a default value. If the key is not found, it will return an empty list []
        values = self.store.get(key, [])

        # binary search
        leftPointer = 0
        rightPointer = len(values) - 1

        while leftPointer <= rightPointer:
            midPointer = (leftPointer + rightPointer) // 2
            # The midPointer is an index. Remember, values is a LIST of pairs.
            # We find the middle element in the list of pairs. It turns out to be [bar, 3]
            # Then, we find the timestamp of the pair. The pair's index 0 = bar, and 1 = 3
            # So, using the index 1 accesses a pair's timestamp 

            # If it's a valid timestamp, save it and then eliminate the left so we can get
            # as close to the given timestamp as possible
            if values[midPointer][1] <= timestamp:
                result = values[midPointer][0] # Save the value, not timestamp
                leftPointer = midPointer + 1
            else: # The timestamp we are on is greater than the one we are trying to get
            # Basically, it's invalid, don't save it, eliminate the right side
                rightPointer = midPointer - 1

        return result
