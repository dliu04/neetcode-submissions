class Solution:
    # at each index, go 
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # Pair of elements: (index, height)

        for i, h in enumerate(heights):
            start = i
            # The top of the stack's height is greater than the height we just reached
            while stack and stack[-1][1] > h: 
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea