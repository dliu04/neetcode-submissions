class Solution:
    # General idea:
    # Create a stack and add a temp on it
    # If it is greater than any previous temps, pop previous temps from stack
    # and save number of days in result array
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index] = accessors being [0, 1]

        for i, temp in enumerate(temperatures):
            # Stack[-1 being the pair on the top of stack][temperature accessor being index 0]
            while stack and temp > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = (i - stackInd) # Num days it took to find greater temp
            stack.append([temp, i])

        return res