# This is the same as the water container one, except slightly more complicated
# I believe this will still involve two pointers (obv)

# I think both pointers should start on the left side
# Send one out ahead, for each time the right pointer is equal to or greater than the left pointer, add it
# to the water count

# The only time leftPointer should increment is via teleporting to rightPointer

# Psuedocode:
# Use i to loop through the array
# LeftPointer starts at 0, rightPointer starts at 1
# If height[leftPointer] <= height[rightPointer], set leftPointer as rightPointer, shift rightPointer += 1
# send rightPointer out ahead to find a value greater than or equal

# The actually correct psuedocode:
# leftPointer on left side, rightPointer on right side
# two variables, maxLeft and maxRight = height[leftPointer], height[rightPointer]
# Shift the smaller number over towards the center
# take the min(R, L) - height[i] > 0, add it to totalWater
# 

 
class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater = 0

        # If the array is empty
        if not height: return 0

        leftPointer = 0
        rightPointer = len(height) - 1
        leftMax, rightMax = height[leftPointer], height[rightPointer]

        while leftPointer < rightPointer:
            if leftMax < rightMax:
                # shift leftPointer
                leftPointer += 1
                # Update the tallest left
                leftMax = max(leftMax, height[leftPointer])
                # Updated the leftMax so this computation will not be negative
                totalWater += leftMax - height[leftPointer]
            else:
                # shift rightPointer   
                rightPointer -= 1
                # Update the tallest right
                rightMax = max(rightMax, height[rightPointer])    
                # Updated rightMax so this computation will not be negative
                totalWater += rightMax - height[rightPointer]

        return totalWater 
