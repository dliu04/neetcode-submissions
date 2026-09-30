# Is there a limit to how long a substring can be? Or can it be the length of the entire array?
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use a set called seen, store unique characters in there
        # Sliding window technique
        # Leftpointer only really serves as a "bookmark" to an index to calculate the length later on.
        # First, leftPointer and rightPointer start off at zero
        # Check if rightPointer is in seen. If not, skip the while loop.
        # Add the rightPointer to the set. 
        # Determine which is greater: the maxlength or the rightpointer - leftpointer + 1 (current substring length)
        # If rightPointer is in seen:
            # Remove characters from the left until the rightPointer is gone
            # Shift the leftPointer over
            # We remove characters from the left until the number is no longer there
            # there is no way the maximum length can be any bigger if that character still exists
            # within our substring. Remove elements up until that character, then carry forward.
            # This is what makes our window a sliding window.

        seen = set()
        leftPointer = 0
        maxLength = 0
        
        # Right pointer starts at zero
        for rightPointer in range(len(s)):
            while s[rightPointer] in seen:
                seen.remove(s[leftPointer])
                leftPointer += 1
            seen.add(s[rightPointer])
            maxLength = max(maxLength, rightPointer - leftPointer + 1)

        return maxLength