class Solution:
    # Can a string be empty?

    def encode(self, strs: List[str]) -> str:
        # Maybe encode can just create a new string by catting strings together
        # and then use a strange combination of characters as a delimiter?
        newString = ""

        for string in strs:
            newString += string
            newString += "%$&"
        
        return newString
            

    def decode(self, s: str) -> List[str]:
        # Assuming s is the one we just encoded
        listString = s.split("%$&")
        # We know there is a delimiter at the very end, which generated a new blank space.
        # destroy the new blank space.
        listString.pop()
        return listString
