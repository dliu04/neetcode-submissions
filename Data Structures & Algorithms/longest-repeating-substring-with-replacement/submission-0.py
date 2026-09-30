# Questions:
# Can there be multiple characters instead of just two unique characters?

# Answer: It should not matter
# Solution:
# You should use two pointers, leftpointer on the left and rightpointer just one off from the left.
# If the window length - most frequent character in window <= k, then that is a valid length


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # This counts the frequency of each character. Useful for determining most frequent char
        res = 0

        leftPointer = 0
        for rightPointer in range(len(s)):
            count[s[rightPointer]] = 1 + count.get(s[rightPointer], 0) # Inits value to 0 if it doesn't exist

            # while the window length - most frequent character is bigger than k
            # remove one count from the dictionary (we are shrinking the window so it makes sense)
            # increment the leftPointer
            while (rightPointer - leftPointer + 1) - max(count.values()) > k:
                count[s[leftPointer]] -= 1
                leftPointer += 1

            # If this while loop isn't tripped, rightPointer naturally increments anyway

            # Result = the max between the current result and the window length
            res = max(res, rightPointer - leftPointer + 1)

        # Loop exits when rightPointer reaches the very end
        return res