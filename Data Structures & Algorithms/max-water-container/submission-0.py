# Initial Problem Analysis:
# It looks like we need to find the largest area in an array
# The walls have to be equal to or greater than in order to hold water to the brim

# I think we can use a two pointer algorithm and then compare every single number to one another
# The important thing is that you need to take height and width into account

# Hint: we should move the pointer with the smaller height. Why?
# I think we should move the pointer with the smaller height because every single time we move 
# the pointer, we are shrinking the area by a lot. Therefore, we should move the smaller one in hopes of mitigating
# that difference by finding a taller height.

# Another key difference is that the water only cares about the smaller pointer's height. It will only
# max out at that level, regardless of how tall the other bigger pointer might be. Therefore, it would 
# be smart to move the smaller pointer around to see how tall we can get.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        leftPointer = 0
        rightPointer = len(heights) - 1

        while leftPointer < rightPointer:
            # First, calculate the amount of water it can hold 
            currentArea = (rightPointer - leftPointer) * (min(heights[rightPointer], heights[leftPointer]))
            if currentArea > maxWater:
                maxWater = currentArea

            # Then, check which one is taller than the other
            # Change the pointer of whichever one is smaller
            if heights[leftPointer] < heights[rightPointer]:
                leftPointer += 1
            elif heights[leftPointer] > heights[rightPointer]:
                rightPointer -= 1
            else:
                leftPointer += 1
        
        return maxWater