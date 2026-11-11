class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # default values
        stack = [] # value pair: [temp, index] <- [0 = temp, 1 = index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # top of stack temp
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd) # num of days to find greater temp
            stack.append([t, i])
        return res