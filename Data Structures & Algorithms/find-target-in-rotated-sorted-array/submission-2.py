# First, find the middle value
# if the target is equal to nums[mid], just return that index

# If the middle pointer and left pointer are on the same segment:
    # Check the right side. If target is within right, abandon left

# If the middle pointer and right pointer are on the same segment:
    # Check the left side. If the target is within left, abandon right

# Why do we care if leftPointer/rightPointer share the same segment with mid?
# We care about what segment midPointer is on because we use midPointer as a
# basis 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftPointer = 0
        rightPointer = len(nums) - 1

        while leftPointer <= rightPointer:
            midPointer = (leftPointer + rightPointer) // 2
            
            if target == nums[midPointer]:
                return midPointer

            # Both numbers are in the left segment
            if nums[midPointer] >= nums[leftPointer]:
                # If the target is on the right segment
                if target > nums[midPointer] or target < nums[leftPointer]:
                    leftPointer = midPointer + 1
                else:
                    rightPointer = midPointer - 1

            # right sorted portion
            else:
                if target < nums[midPointer] or target > nums[rightPointer]:
                    rightPointer = midPointer - 1
                else:
                    leftPointer = midPointer + 1

        return -1
        