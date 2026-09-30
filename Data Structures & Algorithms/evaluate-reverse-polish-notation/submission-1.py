# Questions to ask:
# When we encounter an operator, are we always guaranteed
# two previous integers before it in the stack?

# Code explanation:
# Use a stack to keep track of values
# If there is an operator, pop two previous values and append the
# result to the stack
# If it's just a number, append that number to the stack 
# to be used in the next operation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
            else:
                stack.append(int(token))

        return stack[0]