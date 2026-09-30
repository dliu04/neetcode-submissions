# Binary Search Basics
# Prerequisite: the array must be sorted
# General idea: get the middle of the array
# if the condition is guaranteed to be on one side, remove the other side
# and search the correct one only

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Two pointers
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
            

        # In the case that the left pointer is greater than the right pointer,
        # that means the value does not exist in the array
        return -1
