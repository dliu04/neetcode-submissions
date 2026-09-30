class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paran if openCount < n
        # only add a closing paran if closedCount < openCount
        # valid if and only if openCount == closedCount == n

        stack = []
        res = []

        def backtrack(openCount, closedCount):
            if openCount == closedCount == n:
                res.append("".join(stack)) # take every character from the stack and join them
                return
            
            if openCount < n:
                stack.append("(")
                # Recursion
                backtrack(openCount + 1, closedCount)
                stack.pop()

            if closedCount < openCount:
                stack.append(")")
                backtrack(openCount, closedCount + 1)
                stack.pop()

        backtrack(0, 0)
        return res