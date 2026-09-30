class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Maybe there is a way to "store" products we have already seen before so we don't have
        # to calculate it every single time?

        # How do we iterate through the array, get all the products only once?
        result = []
        product = 1
        containsZero = False
        containsZeroIndex = 0
        containsTwoZeroes = False

        for i in range(len(nums)):
            if nums[i] == 0 and containsZero == False:
                containsZero = True
                containsZeroIndex = i
                continue
            elif nums[i] == 0 and containsZero == True:
                containsTwoZeroes = True
                break
            product *= nums[i]
        
        for i in range(len(nums)):
            if containsZero == True and containsTwoZeroes == False:
                # Populate the array with zeroes except for the index that it contains in
                result = [0] * len(nums)
                result[containsZeroIndex] = product
            elif containsTwoZeroes == True:
                result = [0] * len(nums)
            else:
                result.append(int(product / nums[i]))
        
        return result 
