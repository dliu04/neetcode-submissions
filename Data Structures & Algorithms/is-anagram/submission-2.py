class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {} # hashmaps

        # Count the characters
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # Default value 0
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # Compare each character counts
        for c in countS:
            if countS[c] != countT.get(c, 0): # In case if key doesn't exist
                return False

        return True
            