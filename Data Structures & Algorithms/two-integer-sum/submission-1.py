class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Will the numbers always be in order from least to greatest?
            # It does not say, so we should assume nums can be out of order.

        # If there are two answers [0,3] and [1,2], both should be accepted,
        # so as long as the first number in the first answer is smaller.

        # I don't think sorting is necessary.

        previouslyViewedNumbers = {}

        # Enumerate returns an index and the value
        # so i is index and n is the number at that index
        for i, n in enumerate(nums):
            difference = target - n
            if difference in previouslyViewedNumbers:
                # Assuming previouslyViewedNumbers index is smaller
                return[previouslyViewedNumbers[difference], i]
            # Else add the current num to the previouslyViewedNumbers
            # Stored as a number/index key/value pair
            previouslyViewedNumbers[n] = i
            
        return []