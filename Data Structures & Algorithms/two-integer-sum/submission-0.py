class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Will the numbers always be in order from least to greatest?
            # It does not say, so we should assume nums can be out of order.

        # If there are two answers [0,3] and [1,2], both should be accepted,
        # so as long as the first number in the first answer is smaller.

        # I don't think sorting is necessary.

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): # Starting from i + 1 (index above), ending in len(nums)
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        # Assume that a pair always exists. Therefore,
        # if it returns 0,0 then something is wrong with the code.
        return [0,0]