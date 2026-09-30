class Solution:
    # Can a string be empty?

    def encode(self, strs: List[str]) -> str:
        newString = ""

        for string in strs:
            newString += str(len(string))
            newString += "#"
            newString += string
        
        return newString
            

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # Getting the number
            j = i
            while s[j] != "#":
                j += 1 # Increments from first num till delimiter
            length = int(s[i:j]) # Gets the string from starting index to ending index. Converts into int.
            
            # From index j + 1 (the first letter of the word), go until the index[length]
            # Append the result to result
            result.append(s[j + 1 : j + 1 + length]) # Hella compensating for the delimiter
            # Update the index to start at the next number
            i = j + 1 + length

        return result