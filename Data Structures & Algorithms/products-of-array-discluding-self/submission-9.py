class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Left product of [i] multiplied by the right product of [i]

        # create result array 

        # Create variables for prefixInt, postfixInt both set as 1
        # First iteration of nums
            # Set prefix of result at index i to prefixInt
            # Multiply prefixInt by nums[i]
        # Second iteration of nums starting from nums[len(nums)]
            # Multiply result at index i to the postfixInt
            # Multiply postfixInt by nums[i]

        # return the result
        

        # 1 2 3 4 <- nums
        # 1 1 2 6 <- first iteration
        # 24 12 8 6 <- second iteration
        # That is what we want!

        result = []
        prefixInt = 1
        postfixInt = 1
        
        for i in range(len(nums)):
            result.append(prefixInt)
            prefixInt *= nums[i]
        
        # Iterate backwards
        i = len(nums) - 1
        while i >= 0:
            result[i] *= postfixInt
            postfixInt *= nums[i]
            i -= 1
        
        return result