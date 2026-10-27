class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer1 = 0
        pointer2 = len(s) - 1

        while pointer1 < pointer2:
            # If not an ignored character
            while pointer1 < pointer2 and not self.alphaNum(s[pointer1]):
                pointer1 += 1
            while pointer2 > pointer1 and not self.alphaNum(s[pointer2]):
                pointer2 -= 1
            
            if s[pointer1].lower() != s[pointer2].lower():
                return False

            pointer1 += 1
            pointer2 -= 1

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
