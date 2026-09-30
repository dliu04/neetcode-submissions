class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # Init count dictionary
        res = 0 # length of longest substring

        # General idea is:
        # Use the count dictionary, letter as a key and the frequency as the value
        # If the sliding window - most frequent character > k, adjust the window
        # This is because (sliding window - most frequent character) = num characters we have to replace

        leftPointer = 0
        for rightPointer in range(len(s)):
            # Add one to the corresponding letter for bookkeeping
            count[s[rightPointer]] = 1 + count.get(s[rightPointer], 0) # inits value to zero if no value exists

            # While num characters to be replaced exceeds K
            while (rightPointer - leftPointer + 1) - max(count.values()) > k:
                # Remove one leftPointer count and adjust the window
                count[s[leftPointer]] -= 1
                leftPointer += 1
            
            # The answer will either be a previously saved result or the length of the current valid sliding window
            res = max(res, rightPointer - leftPointer + 1)

        return res

    # The general idea of a sliding window is:
    # You have two pointers, a left and a right pointer. They both start on the same side, usually the left side.
    # You usually send the right pointer forward, and due to some condition, you may need to send the left pointer forward 
    # or adjust the right pointer's incrementation.
    # The rightPointer is usually the incrementer, so it exists within a for loop. The leftPointer is usually conditional,
    # which should be in a while loop with some condition within the for loop.

