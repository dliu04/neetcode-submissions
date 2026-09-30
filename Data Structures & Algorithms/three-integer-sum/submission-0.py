class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the input array
        # Use three pointers. Leftmost, left, and right.
        # Leftmost should only increment once per loop. 
        # Left and right will do essentially the same thing as 
        # sorted twosum did in the past.
        result = []
        nums.sort()

        # "Leftmost Pointer" can be i
        for i, num in enumerate(nums):
            # If leftmost pointer is a duplicate
            if i > 0 and num == nums[i - 1]:
                continue
                # We want to continue because we already determined
                # the answers for this duplicate value
            leftPointer = i + 1
            rightPointer = len(nums) - 1

            while leftPointer < rightPointer:
                if (nums[leftPointer] + nums[rightPointer]) == -num:
                    result.append([num, nums[leftPointer], nums[rightPointer]])
                    leftPointer += 1
                    # This line of code below will make sure that 
                    # the leftPointer will be a new value instead of a duplicate
                    # This is because duplicate values violate the nature of the 
                    # solution
                    while nums[leftPointer] == nums[leftPointer - 1] and leftPointer < rightPointer:
                        leftPointer += 1
                elif (nums[leftPointer] + nums[rightPointer]) < -num:
                    leftPointer += 1
                elif (nums[leftPointer] + nums[rightPointer]) > -num:
                    rightPointer -= 1
        
        return result