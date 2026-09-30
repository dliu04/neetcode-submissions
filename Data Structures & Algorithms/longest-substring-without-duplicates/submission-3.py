class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        leftPointer = 0
        seen = set()

        for rightPointer in range(len(s)):
            while s[rightPointer] in seen:
                # remove values up until most recent character
                seen.remove(s[leftPointer]) 
                leftPointer += 1
            seen.add(s[rightPointer])
            maxLength = max(maxLength, rightPointer - leftPointer + 1) # +1 is to offset index

        return maxLength