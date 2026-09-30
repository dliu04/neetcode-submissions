class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Assuming that the numbers are in increasing order
        # Assuming that there is always single number that is missing
        
        # Sort the nums
        nums.sort()

        expectedNumber = 0
        maxRange = len(nums)
        
        # Loop through the list
        for num in nums:
            # On every iteration
            # Check if the current number does not equal the expected number
            if num != expectedNumber:
                # if it is, Return expected number
                return expectedNumber

            # Else, increment and restart the loop
            expectedNumber = expectedNumber + 1

        # If the expected number is one out of the range
        return maxRange


