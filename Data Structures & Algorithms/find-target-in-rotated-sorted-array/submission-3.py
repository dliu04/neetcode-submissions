# First, find the middle value
# if the target is equal to nums[mid], just return that index

# If the middle pointer and left pointer are on the same segment:
    # Check the right side. If target is within right, abandon left

# If the middle pointer and right pointer are on the same segment:
    # Check the left side. If the target is within left, abandon right

# Why do we care if leftPointer/rightPointer share the same segment with mid?
# We care about what segment midPointer is on because we use midPointer as a
# basis to figure out which half is SORTED.

# Remember: Binary search is only effective on sorted segments.

# In a rotated array, at least one segment is always properly sorted.
# Example: 4 5 6 7 8 1 2 3 
#                ^ midpoint
# 8 1 2 3 is not sorted, but 4 5 6 7 is. 
# Check if 4 <= target <= 7. If so, we can pursue this segment.
# If not, then we can pursue the right segment. Even if it's unsorted, we
# still can reperform binary search on this segment to attempt to find the
# correct answer.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftPointer = 0
        rightPointer = len(nums) - 1

        while leftPointer <= rightPointer:
            midPointer = (leftPointer + rightPointer) // 2
            
            if target == nums[midPointer]:
                return midPointer

            # Both numbers are in the left segment
            # Meaning, this segment is properly sorted
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
        