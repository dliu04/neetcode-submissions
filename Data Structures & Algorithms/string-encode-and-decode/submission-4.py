class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        # Encode it with length + delimiter
        for string in strs:
            encodedString += str(len(string))
            encodedString += "#"
            encodedString += string

        return encodedString

    def decode(self, s: str) -> List[str]:
        i = 0
        decodedStrings = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            string = s[j + 1 : j + 1 + length]
            decodedStrings.append(string)
            i = j + 1 + length

        return decodedStrings
