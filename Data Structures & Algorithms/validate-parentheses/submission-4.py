class Solution:
    def isValid(self, s: str) -> bool:
        deck = collections.deque()
        validPairs = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        for i in range(len(s)):
            # Check if it's closing bracket
            # and deck is not empty
            if s[i] in validPairs.values() and deck:
                # Check if the most recently added element matches the
                # closing bracket
                if validPairs[deck[-1]] == s[i]:
                    deck.pop()
                else:
                    return False
            elif s[i] in validPairs.keys():
                # If it means that it's an opening bracket
                deck.append(s[i])
            else:
                return False

        # If there are elements still within the deque
        if deck:
            return False
        else:
            return True