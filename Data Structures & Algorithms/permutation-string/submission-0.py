# Question:
# Can a string be empty?

# Use the sliding pointer technique
# Start both pointers on the left side
# If the window contains the permutation of characters we need, return true
# Else, adjust the window

# We know the window cannot exceed longer than s1 length, so that's how we adjust the left pointer
# We know that the window cannot exceed shorter than s1 length, so that's how we adjust the right pointer

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = {}
        s1Freq = {} # Freq of the original s1 string
        result = False

        # First count the frequencies of s1
        for char in s1:
            s1Freq[char] = 1 + s1Freq.get(char, 0)

        leftPointer = 0
        for rightPointer in range(len(s2)):
            seen[s2[rightPointer]] = 1 + seen.get(s2[rightPointer], 0)

            # If the sliding window exceeds the length of s1
            while (rightPointer - leftPointer + 1) > len(s1):
                # Shift the left pointer over
                seen[s2[leftPointer]] -= 1
                # Remove the key if value is 0
                if seen[s2[leftPointer]] == 0:
                    del seen[s2[leftPointer]]
                leftPointer += 1

            # How about we count the frequencies of s1 and compare it with s2
            if s1Freq == seen:
                return True

        return False