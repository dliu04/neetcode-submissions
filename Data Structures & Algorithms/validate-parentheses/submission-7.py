class Solution:
    def isValid(self, s: str) -> bool:

        # Push when L bracket
        # Pop when R bracket
        # When R bracket, check if top of stack has corresponding L bracket before popping
            # If corresponds, continue
            # If not, return False
        
        # Return True

        if not s:
            return False

        stack = []

        for i in range(len(s)):
            if s[i] == "[" or s[i] == "(" or s[i] == "{":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                
                if s[i] == "]" and stack[-1] == "[":
                    stack.pop()
                elif s[i] == ")" and stack[-1] == "(":
                    stack.pop()
                elif s[i] == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False

        return len(stack) == 0