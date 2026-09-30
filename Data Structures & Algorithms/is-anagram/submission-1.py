class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams can contain the same characters, but 
        # does it have to be the same amount of characters?

        if len(s) != len(t):
            return False

        # Iterate through the string (assuming equal lengths)
        # If a character from string 1 exists in string 2, delete both
        # characters from the string.

        # Theoretically, the strings should "eliminate" one another until 
        # there are no characters left.

        for char in s:
            for charTwo in t:
                if char == charTwo:
                    s = s.replace(char, '', 1) # Replace the character with blank once
                    t = t.replace(charTwo, '', 1)
                    break
        
        if len(s) == 0 and len(t) == 0:
            return True
        else:
            return False