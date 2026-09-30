class Solution:
    # Can a string be empty?

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString += str(len(string))
            encodedString += "#"
            encodedString += string
        return encodedString

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        # i can be the counter by chunk
        while i < len(s):
            j = i
            # Increment until delimiter is reached
            while s[j] != "#":
                j += 1
            # ^ I think this increments till the index right before the delimiter
            # Slice to obtain number
            length = int(s[i : j])
            # Append the result
            result.append(s[j + 1 : j + 1 + length])
            # Increment i appropriately
            i = j + 1 + length
        
        return result
