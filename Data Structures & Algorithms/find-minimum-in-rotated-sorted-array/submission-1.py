# So if the array was rotated "n" times, that means the last n numbers
# were placed at the beginning of the array
# We are not given n

# Elements in this array are unique: is that a hint?

# If in left sorted array, discard left and check right since left is 
# always greater 

# Do a binary search to locate the cutoff where the array was rotated

# Start, place left pointer on left side, right pointer on right side
# and a midpoint
# a midpoint and another pointer will always be on the same side
# You can use this condition to eliminate the greater side

# if leftPointer and mid are in the same segment, and leftPointer's value is smaller
# than middlePointer's value, then the min value will be in the right part.
# If rightPointer and mid are in the same segment, and 
# the middle value is smaller than the right pointer, then the min value
# is in the leftPointer.

# What if the array is 4 5 6 7? We can't assume that the minimum value
# is immediately in the right segment.
# A fix for that issue is to check if the given array is in ascending order
# via a simple leftPointer < rightPointer check.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]

        leftPointer = 0
        rightPointer = len(nums) - 1

        while leftPointer <= rightPointer:
            # First, check if the segment is split
            # If the current segment is in ascending order:
            if nums[leftPointer] < nums[rightPointer]:
                minimum = min(minimum, nums[leftPointer])
                break

            midPoint = (leftPointer + rightPointer) // 2
            minimum = min(minimum, nums[midPoint])
            
            # If the current segment is not in ascending order:
            # if midpoint value is greater than leftpointer, then
            # we are currently in the segment that contains greater values.
            # eliminate the left segment:
            if nums[leftPointer] <= nums[midPoint]:
                leftPointer = midPoint + 1
            else:
                rightPointer = midPoint - 1

        return minimum





        