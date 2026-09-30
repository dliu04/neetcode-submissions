# Is this problem case sensitive? does ASDFJ not contain df?

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Return the shortest string that contains all characters in substring t
        # if no substring exists, return a ""

        # I am thinking that we just use a frequency count dictionary for t first
        # then count the frequency of chars in sliding window and then ultimately compare
        # the valid keys and values

        tFreq = {}
        window = {}
        res = ""
        resLen = float("infinity") # Use this number instead of zero cuz we are trying to find smallest substring

        # First, save the frequencies of T in a hashmap:
        for char in t:
            tFreq[char] = 1 + tFreq.get(char, 0)

        # The tricky part is that it has to be the SHORTEST substring, which I don't really know how to do
        # Hint: Save the result substring and only update it if a shorter substring is found.

            # Use a "Have" counter to count the number of chars we have that sFreq needs
            # If s[rightPointer] == char that we need
                # Save the frequency in Window
            # If Window has all the chars we need (if Have == tFreq.count)
                # Save the string into result if it is shorter
                # Use a while loop to pop chars from the left until Window does not have chars we need anymore
            # If Window counter does not have the chars in t
                # Keep incrementing the rightPointer (for loop)

        have = 0
        need = len(tFreq)
        leftPointer = 0

        for rightPointer in range(len(s)):
            # Add the right pointer to window
            char = s[rightPointer]
            window[char] = 1 + window.get(char, 0)

            # If the character is in t and the frequencies are equal
            if char in tFreq and window[char] == tFreq[char]:
                have += 1

            while have == need:
                if (rightPointer - leftPointer + 1) < resLen:
                    resLen = (rightPointer - leftPointer + 1)
                    # Python includes the left but not the right during slicing
                    # Add one to offset this
                    res = s[leftPointer : rightPointer + 1]
                # Start removing characters from the left
                removeChar = s[leftPointer]
                window[removeChar] -= 1
                # If it was in tFreq, decrement Have
                # and check if the window is no longer sufficient
                if removeChar in tFreq and window[removeChar] < tFreq[removeChar]:
                    have -= 1
                leftPointer += 1

            
        return res