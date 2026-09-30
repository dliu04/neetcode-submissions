# Questions to ask:
# When we encounter an operator, are we always guaranteed
# two previous integers before it in the stack?

# Code explanation:
# If there is an operator, pop two previous values and append the
# result to the stack
# If it's just a number, append that number to the stack 
# to be used in the next operation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(c))

        # Only one value left
        return stack[0]