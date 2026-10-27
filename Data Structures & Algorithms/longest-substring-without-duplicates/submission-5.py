class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        result = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet: # If rightPointer is a duplicate char
                # Increment leftPointer
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)
        
        return result